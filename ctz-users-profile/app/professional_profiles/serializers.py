from rest_framework import serializers
from core.professional_profile import ProfessionalProfile


class ProfessionalProfileSerializer(serializers.ModelSerializer):
    """professional profile serializer"""

    class Meta:
        model = ProfessionalProfile
        fields = "__all__"
