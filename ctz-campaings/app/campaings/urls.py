from django.urls import path
from .views import CampaingView

app_name = "campaing"

urlpatterns = [
    path("user/campaing/list/<int:pk>", CampaingView.as_view(
             {"get": "list"}
         ), name="campaing-list"),
    path("user/campaing", CampaingView.as_view(
             {"post": "create"}),
         name="campaing-create"
    ),
    path("user/campaing/<int:pk>", CampaingView.as_view(
             {"get": "retrieve", "put": "update", "delete": "delete"}),
         name="campaing-detail"
    )
]
