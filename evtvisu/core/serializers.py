from rest_framework import serializers
from .models import  EnYear




class EnYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnYear
        fields = '__all__'
