from rest_framework import serializers
from manager.models import Trip
class TripSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'