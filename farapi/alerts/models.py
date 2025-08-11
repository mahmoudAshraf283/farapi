from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Alert(models.Model):
    ALERT_TYPES = (
        ('threshold', 'Threshold'),
        ('duration', 'Duration'),
    )
    CONDITIONS = (
        ('above', 'Above'),
        ('below', 'Below'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    condition = models.CharField(max_length=10, choices=CONDITIONS)
    value = models.FloatField()
    duration = models.IntegerField(default=0)  # Duration in minutes for duration alerts
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    # For duration alerts - track when condition started being met
    condition_met_since = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.symbol} {self.condition} {self.value}"

class TriggeredAlert(models.Model):
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE)
    triggered_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    email_sent = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Triggered: {self.alert.symbol} at {self.price}"
