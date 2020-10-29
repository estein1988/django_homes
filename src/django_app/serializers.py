from rest_framework import serializers

from .models import Home

class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = ('id', 'photo', 'price', 'bed', 'bath', 'street', 'city', 'state', 'zip_code', 'lat_long')