from django.db import models
from .abstracts import AbstractProfile
from core.user import User


class ContactAddress(AbstractProfile):
    """contact Address profile"""
    dni = models.CharField(max_length=30)
    delete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.address
   
    @classmethod
    def list(cls, current_user):
        all = cls.objects.filter(user=current_user, delete=False)
        return all

    @classmethod
    def current(cls, pk, current_user, delete=False):
        current_contact = cls.objects.get(
            id=pk, user=current_user, delete=delete
        )
        return current_contact

    @classmethod
    def create(cls, request):
        try:
            cls.objects.create(
                address=request.data.get("address"),
                street=request.data.get("street"),
                cellphone=request.data.get("cellphone"),
                email=request.data.get("email"),
                description=request.data.get("description"),
                dni=request.data.get("dni"),
                user=request.user
            )
            return True
        except:
            return False

    @classmethod
    def update(cls, pk, request):
        try:
            contact_updated = cls.current(pk, request.user)
            contact_updated.address = request.data.get("address")
            contact_updated.street = request.data.get("street")
            contact_updated.cellphone = request.data.get("cellphone")
            contact_updated.description = request.data.get("description")
            contact_updated.dni = request.data.get("dni")
            contact_updated.save()
            return True
        except:
            return False

    @classmethod
    def erase(cls, pk, request):
        try:
            contact_delete = cls.current(pk, request.user) 
            contact_delete.delete = True
            contact_delete.save()
            return True
        except:
            return True

    
