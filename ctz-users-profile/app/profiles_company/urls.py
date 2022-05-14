from django.urls import path
from .views import ProfileCompanyView

app_name = "profile_company"

urlpatterns = [
    path("user/profile-company", ProfileCompanyView.as_view(
             {"get": "list", "post": "create"}),
         name="profile-company-create"
    ),
    path("user/profile-company/<int:pk>", ProfileCompanyView.as_view(
             {"get": "retrieve", "put": "update", "delete": "delete"}),
         name="profile-company-detail"
    )
]
