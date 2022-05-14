from contact_address import serializers
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import SocialNetworkSerializer
from core.social_network import SocialNetwork


class SocialNetworkView(viewsets.ModelViewSet):
    """social network from current user"""

    serializer_class = SocialNetworkSerializer
    queryset = SocialNetwork.objects.all()

    def list(self, request):
        try: 
            all = SocialNetwork.list(request)
            serializer = self.serializer_class(all, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        try:
            single = SocialNetwork.current(pk, request)
            serializer = self.serializer_class(single)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def create(self, request):
        try:
            created = SocialNetwork.create(request)
            if created:
                return Response(
                    {"data": created, "msg": "social network created"},
                    status=status.HTTP_201_CREATED
                )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"},
                status=status.HTTP_400_BAD_REQUEST
            ) 

    def update(self, request, pk=None):
        try:
            updated = SocialNetwork.update(pk, request)
            if updated:
                return Response(
                    {"data": True, "msg": "social network created"},
                    status=status.HTTP_201_CREATED
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
            deleted = SocialNetwork.erase(pk, request)
            if deleted:
                return Response(
                    {"data": True, "msg":"social network deleted"},
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
