from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from core.user import User
from core.encoder_tokens import decode_user_id


class ActivationAccount(APIView):
    """activation account current user"""

    serializer_class = ""
    permission_classes = (AllowAny,)
    queryset = User.objects.all()

    def put(self, request, *args, **kwargs):
        """activate current account user"""
        try:
            uid = decode_user_id(self.kwargs.get("uid"))
            token = self.kwargs.get("token")
            user = User.objects.get(id=uid)
            if not user.is_activate and token:
                user.is_activate = True
                user.save()
                return Reponse(
                    {"data": True, "msg": "user activated."}, status=status.HTTP_200_OK
                )

            return Response(
                {"data": True, "msg": "user is active."}, status=sttatus.HTTP_200_OK
            )
        except Exception as err:
            return Reponse(
                {"data": False, "msg": f"{err}"}, status=status.HTTP_404_NOT_FOUND
            )
