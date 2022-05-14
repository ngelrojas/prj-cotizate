from django.urls import path, re_path
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from users import views
from users import activation
from .custom_user_login import CustomLoginUser

app_name = "user"

urlpatterns = [
    path("auth", ObtainJSONWebToken.as_view(serializer_class=CustomLoginUser)),
    path("auth-token-refresh", refresh_jwt_token),
    path("auth-token-verify", verify_jwt_token),
    path("user", views.CreateUserView.as_view(), name="create"),
    path(
        "user/<int:pk>",
        views.UpdateUserView.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="update",
    ),
    re_path(
        r"^activate/(?P<uid>[0-9A-Za-z_\-]+)/"
        "(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})$",
        activation.ActivationAccount.as_view(),
        name="activation",
    ),
    path(
        "recovery-password",
        views.RecoveryPasswordUser.as_view({"post": "create"}),
        name="recovery-password",
    ),
    path(
        "recovery-confirm",
        views.RecoveryPwdConfirm.as_view({"put": "update"}),
        name="recovery-confirm",
    ),
]
