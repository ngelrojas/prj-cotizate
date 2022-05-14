from django.urls import path
from .views import ProfessionalProfileView

app_name = "professional_profile"

urlpatterns = [
    path("user/professional-profile", ProfessionalProfileView.as_view(
             {"get": "list", "post": "create"}),
         name="professional-profile-create"
    ),
    path("user/professional-profile/<int:pk>", ProfessionalProfileView.as_view(
             {"get": "retrieve", "put": "update", "delete": "delete"}),
         name="professional-profile-detail"
    )
]
