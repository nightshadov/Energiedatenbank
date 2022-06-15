from rest_framework import serializers
from .models import ExperimentLog, AlmemoLog, EnYear




class EnYearSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnYear
        fields = '__all__'
