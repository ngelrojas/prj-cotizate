from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from .serializers import ContactAddreSerializer 
from core.contact_address import ContactAddress


class ContactAddreView(viewsets.ModelViewSet):
    """create contact address from current user"""

    serializer_class = ContactAddreSerializer
    queryset = ContactAddress.objects.all()


    def list(self, request):
        """list all contact address
            from current user logged
        """
        try:
            contact_all = ContactAddress.list(request.user)
            serializer = self.serializer_class(contact_all, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """get contact address from current user logged"""
        try:
            single_contact = ContactAddress.current(pk, request.user)
            serializer = self.serializer_class(single_contact)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        """create contact address from current user"""
        try:
            created = ContactAddress.create(request)
            if created:
                return Response(
                    {"data": True, "msg": "contact created"},
                    status=status.HTTP_201_CREATED
                )
            return Response(
                {"data": False, "msg": "something problem"},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """update contact address form current user logged"""
        try:
            contact_updated = ContactAddress.update(pk, request)
            if contact_updated:
                return Response(
                    {"data": True, "msg": "contact address updated"},
                    status=status.HTTP_200_OK
                )

            return Response(
                {"data": None, "msg": "data not update"},
                status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """delete soft contact address from current user logged"""
        try:
            contact_deleted = ContactAddress.erase(pk, request)
            if contact_deleted:
                return Response(
                    {"data": True, "msg": "contact address deleted"},
                    status=status.HTTP_204_NO_CONTENT
                )

            return Response(
                {"data": None, "msg": "contact not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"data": None, "msg": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)

