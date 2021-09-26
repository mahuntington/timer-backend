from rest_framework import serializers 
from .models import Session 

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('id', 'seconds', 'created_at', 'time_in_minutes', 'local_time',)

