from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import ProfileCompanySerializer
from core.profile_company import ProfileCompany


class ProfileCompanyView(viewsets.ModelViewSet):
    """profile company from current user"""

    serializer_class = ProfileCompanySerializer
    queryset = ProfileCompany.objects.all()

    def list(self, request):
        """list all profile company"""
        try:
            pc_all = ProfileCompany.list(request.user)
            serializer = self.serializer_class(pc_all, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                satus=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """get profile company from current user"""
        try:
            pc_single = ProfileCompany.current(pk, request.user)
            serializer = self.serializer_class(pc_single)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        try:
            created = ProfileCompany.create(request)
            if created:
                return Response(
                    {"data": created, "msg": "profile company created."},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {"data": False, "msg": f"something wrong return a {created}"},
                status=status.HTTP_404_NO_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )
   
    def update(self, request, pk=None):
        try:
            updated = ProfileCompany.update(pk, request)
            if updated:
                return Response(
                    {"data": True, "msg": "profile company updated"},
                    status=status.HTTP_200_OK
                )
            return Response(
                {"data": False, "msg": f"something wrong return a {updated}"},
                status=status.HTTP_404_NO_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        try:
            deleted = ProfileCompany.erase(pk, request)
            if deleted:
                return Response(
                    {"data": True, "msg":"profile company deleted"},
                    status=status.HTTP_204_NO_CONTENT
                )
            return Response(
                {"data": False, "msg": f"something wrong return a {deleted}"},
                status=status.HTTP_404_NO_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )
