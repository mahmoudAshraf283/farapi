from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Alert, TriggeredAlert
from .serializers import AlertSerializer, TriggeredAlertSerializer

class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Alert.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    @action(detail=True, methods=['post'])
    def toggle_active(self, request, pk=None):
        """Toggle alert active status"""
        alert = self.get_object()
        alert.is_active = not alert.is_active
        alert.save()
        
        serializer = self.get_serializer(alert)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def triggered(self, request):
        """Get all triggered alerts for user"""
        triggered_alerts = TriggeredAlert.objects.filter(alert__user=request.user)
        serializer = TriggeredAlertSerializer(triggered_alerts, many=True)
        return Response(serializer.data)