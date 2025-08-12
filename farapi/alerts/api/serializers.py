from rest_framework import serializers
from ..models import Alert, TriggeredAlert
from django.conf import settings

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = [
            'id', 'symbol', 'alert_type', 'condition', 'value', 
            'duration', 'created_at', 'is_active', 'condition_met_since'
        ]
        read_only_fields = ['condition_met_since', 'is_triggered']
    
    def validate(self, data):
        if data['alert_type'] == 'duration' and data.get('duration', 0) <= 0:
            raise serializers.ValidationError(
                "Duration must be greater than 0 for duration alerts"
            )
        
        if data['symbol'] not in settings.STOCKS:
            raise serializers.ValidationError(
                f"Symbol must be one of: {', '.join(settings.STOCKS)}"
            )
        
        return data

class TriggeredAlertSerializer(serializers.ModelSerializer):
    alert_details = AlertSerializer(source='alert', read_only=True)
    
    class Meta:
        model = TriggeredAlert
        fields = ['id', 'alert', 'alert_details', 'price', 'triggered_at', 'email_sent']