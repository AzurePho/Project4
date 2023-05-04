from rest_framework import serializers
from ..models import Dev

class DevSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dev
        fields = '__all__'