from django.urls import path
from .views import SocialNetworkView

app_name = "social_network"

urlpatterns = [
    path("user/social-network", SocialNetworkView.as_view(
             {"get": "list", "post": "create"}
         ), name="social-network-create"
    ),
    path("user/social-network/<int:pk>", SocialNetworkView.as_view(
             {"get": "retrieve", "put": "update", "delete": "delete"}
         ), name="social-network-detail"
    )
]
