from rest_framework import serializers
from core.profile_company import ProfileCompany


class ProfileCompanySerializer(serializers.ModelSerializer):
    """profile company serializer"""

    class Meta:
        model = ProfileCompany
        fields = "__all__"
