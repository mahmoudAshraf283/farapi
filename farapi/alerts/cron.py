from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from .models import Alert, TriggeredAlert
import requests
import os
api_key = os.getenv("API_KEY")
def get_current_price(symbol):
    url = f"https://api.twelvedata.com/quote?symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f"Error fetching price for {symbol}: {response.text}")
    data = response.json()
    if 'close' in data:
        return float(data['close'])
    else:
        raise ValueError(f"Invalid data for {symbol}: {data}")

def check_alerts():
    # Fetch current prices for all stocks
    prices = {}
    for symbol in settings.STOCKS:
        try:
            prices[symbol] = get_current_price(symbol)
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            continue
    
    # Check each active alert
    for alert in Alert.objects.filter(is_active=True):
        price = prices.get(alert.symbol)
        if price is None:
            continue
        
        condition_met = (
            (alert.condition == 'above' and price > alert.value) or
            (alert.condition == 'below' and price < alert.value)
        )
        
        now = timezone.now()
        
        if condition_met:
            if alert.condition_met_since is None:
                alert.condition_met_since = now
            
            elapsed_minutes = (now - alert.condition_met_since).total_seconds() / 60
            required_duration = alert.duration if alert.alert_type == 'duration' else 0
            
            if elapsed_minutes >= required_duration and not alert.is_triggered:
                triggered = TriggeredAlert.objects.create(
                    alert=alert,
                    price=price
                )
                send_notification(triggered)
                alert.is_triggered = True
        else:
            alert.condition_met_since = None
            alert.is_triggered = False
        
        alert.save()

def send_notification(triggered):
    subject = f"Stock Alert Triggered for {triggered.alert.symbol}"
    message = (
        f"Your {triggered.alert.alert_type} alert for {triggered.alert.symbol} "
        f"has been triggered at price {triggered.price}.\n"
        f"Condition: {triggered.alert.condition} {triggered.alert.value}"
    )
    if triggered.alert.alert_type == 'duration':
        message += f" for {triggered.alert.duration} minutes."
    
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [triggered.alert.user.email],
        fail_silently=False,
    )
    triggered.email_sent = True
    triggered.save()