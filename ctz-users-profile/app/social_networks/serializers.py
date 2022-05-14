from rest_framework import serializers
from core.social_network import SocialNetwork


class SocialNetworkSerializer(serializers.ModelSerializer):
    """social network serializer"""

    class Meta:
        model = SocialNetwork
        fields = "__all__"
