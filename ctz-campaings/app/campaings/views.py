from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import CampaingSerializer
from core.campaing import Campaing


class CampaingView(viewsets.ModelViewSet):
    serializer_class = CampaingSerializer
    queryset = Campaing.objects.all()

    def list(self, request, pk):
        try:
            list_campaing = Campaing.list(request, pk)
            serializer = self.serializer_class(list_campaing, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        try:
            campaing_single = Campaing.current(pk, request)
            serializer = self.serializer_class(campaing_single)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request, pk=None):
        try:
            created = Campaing.create(request)
            if created:
                return Response(
                    {"data": created, "msg": "campaing created."},
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
            updated = Campaing.update(pk, request)
            if updated:
                return Response(
                    {"data": True, "msg": "campaing updated"},
                    status=status.HTTP_200_OK
                )
            return Response(
                {
                    "data": None, 
                    "msg": f"something wrong return a {updated}"
                },
                status=status.HTTP_404_NO_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk=None):
        try:
            deleted = Campaing.erase(pk, request)
            if deleted:
                return Response(
                    {"data": True, "msg": "campaing deleted"},
                    status=status.HTTP_204_NO_CONTENT
                )
            return Response(
                {"data": False, "msg":f"something wrong return a {deleted}"},
                status=status.HTTP_404_NO_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )
