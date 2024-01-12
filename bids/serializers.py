from .models import Bids, BidsHistory
from rest_framework import serializers

class BidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids
        fields = '__all__'
        depth = 1

class BidsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bids
        fields = '__all__'

class BidsHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BidsHistory
        fields = '__all__'
        # depth = 1

class BidsHistoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BidsHistory
        fields = '__all__'