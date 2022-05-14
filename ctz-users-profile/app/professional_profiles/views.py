from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProfessionalProfileSerializer
from core.professional_profile import ProfessionalProfile


class ProfessionalProfileView(viewsets.ModelViewSet):
    """professional profile from current user"""

    serializer_class = ProfessionalProfileSerializer
    queryset = ProfessionalProfile.objects.all()

    def list(self, request):
        """list all professinal profile"""
        try:
            pp_all = ProfessionalProfile.list(request.user)
            serializer = self.serializer_class(pp_all, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """get professional profile from current user logged."""
        try:
            pp_single = ProfessionalProfile.current(pk, request.user)
            serializer = self.serializer_class(pp_single)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_404_NOT_FOUND
            )

    def create(self, request):
        """create professional profile from current user logged."""
        try:
            created = ProfessionalProfile.create(request)
            if created:
                return Response(
                    {"data": created, "msg": "Professional profile created."},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {"data": False, "msg": "something wrong."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def update(self, request, pk=None):
        """update professional profile from current user logged."""
        try:
            updated = ProfessionalProfile.update(pk, request) 
            if updated:
                return Response(
                    {"data": True, "msg": "professional profile updated."},
                    status=status.HTTP_200_OK
                )
            return Response(
                {"data": None, "msg": "data not updated"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        """delete soft professional profile from current user logged."""
        try:
            pp_delete = ProfessionalProfile.erase(pk, request) 
            if pp_delete:
                return Response(
                    {"data": True, "msg": "professional profile deleted."},
                    status=status.HTTP_204_NO_CONTENT
                )

            return Response(
                {"data": None, "msg": "professional profile not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )
