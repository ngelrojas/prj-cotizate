from django.db import models
from .user import User
from .abstracts import AbstractProfile
from autoslug import AutoSlugField

def nameFile(instance, filename):
    fdir = str(instance).replace(" ","_") 
    return '/'.join(['images/profile-company', fdir, filename])

class ProfileCompany(AbstractProfile):
    """profile company"""

    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from="name", always_update=True)
    photo = models.ImageField(upload_to=nameFile, blank=True, null=True)
    nit = models.CharField(max_length=30, blank=True, null=True)
    delete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    @classmethod
    def list(cls, current_user):
        all = cls.objects.filter(user=current_user, delete=False)
        return all

    @classmethod
    def current(cls, pk, current_user, delete=False):
        actual = cls.objects.get(
            id=pk, user=current_user, delete=delete
        )
        return actual

    @classmethod
    def create(cls, request):
        try:
            created = cls.objects.create(
                address=request.data.get("address"),
                street=request.data.get("street"),
                cellphone=request.data.get("cellphone"),
                email=request.data.get("email"),
                description=request.data.get("description"),
                name=request.data.get("name"), 
                photo=request.data["photo"],
                nit=request.data.get("nit"),
                user=request.user
            )
            return created.id
        except Exception as e:
            return e

    @classmethod
    def update(cls, pk, request):
        try:
            single = cls.current(pk, request.user)
            if request.data["photo"]:
                single.photo = request.data["photo"]
            single.address=request.data.get("address")
            single.street=request.data.get("street")
            single.cellphone=request.data.get("cellphone")
            single.email=request.data.get("email")
            single.description=request.data.get("description")
            single.name = request.data.get("name")  
            single.nit = request.data.get("nit")
            single.save()
            return True
        except:
            return False

    @classmethod
    def erase(cls, pk, request):
        try:
            deleted = cls.current(pk, request.user)
            deleted.delete = True
            deleted.save()
            return True
        except:
            return False
