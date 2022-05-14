from rest_framework import serializers
from core.contact_address import ContactAddress


class ContactAddreSerializer(serializers.ModelSerializer):
    """contact address serializer"""

    class Meta:
        model = ContactAddress
        fields = "__all__"


