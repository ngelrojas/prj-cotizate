from django.urls import path
from .views import ContactAddreView

app_name = "contact_address"

urlpatterns = [
    path("user/contact-address", ContactAddreView.as_view(
             {"get": "list", "post": "create"}),
         name="contact-address-create"
    ),
    path("user/contact-address/<int:pk>", ContactAddreView.as_view(
             {"get": "retrieve", "put": "update", "delete": "delete"}),
         name="contact-address-detail"
    )
]
