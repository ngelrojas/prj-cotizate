from rest_framework import serializers
from core.campaing import Campaing


class CampaingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Campaing
        fields = "__all__"
