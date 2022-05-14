from django.db import models
from .user import User
from .abstracts import AbstractProfile
from autoslug import AutoSlugField

def nameFile(instance, filename):
    fdir = str(instance).replace(" ","_") 
    return '/'.join(['images/professional-profile', fdir, filename])


class ProfessionalProfile(AbstractProfile):
    """profilessional profile"""

    headline = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="headline", always_update=True)
    current_position = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    date_begin = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=nameFile, blank=True, null=True)
    experience_years = models.IntegerField(default=0)
    delete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.headline

    @classmethod
    def list(cls, current_user):
        all = cls.objects.filter(user=current_user, delete=False)
        return all

    @classmethod
    def current(cls, pk, current_user, delete=False):
        current_pp = cls.objects.get(
            id=pk, user=current_user, delete=delete
        )
        return current_pp

    @classmethod
    def create(cls, request):
        try:
            created = cls.objects.create(
                address=request.data.get("address"),
                street=request.data.get("street"),
                cellphone=request.data.get("cellphone"),
                email=request.data.get("email"),
                headline=request.data.get("headline"),
                current_position=request.data.get("current_position"),
                description=request.data.get("description"),
                date_begin=request.data.get("date_begin"),
                date_end=request.data.get("date_end"),
                photo=request.data["photo"],
                experience_years=request.data.get("experience_years"),
                user=request.user
            )
            return created.id 
        except Exception as e:
            return e

    @classmethod
    def update(cls, pk, request):
        try:
            single = cls.current(pk, request.user)
            single.address=request.data.get("address")
            single.street=request.data.get("street")
            single.cellphone=request.data.get("cellphone")
            single.email=request.data.get("email")
            single.description=request.data.get("description")
            single.headline = request.data.get("headline")
            single.current_position = request.data.get("current_position")
            single.description = request.data.get("description")
            single.date_begin = request.data.get("date_begin")
            single.date_end = request.data.get("date_end")
            if request.data["photo"]: 
                single.photo = request.data["photo"]
            single.experience_years = request.data.get("experience_years")
            single.save() 
            return True
        except:
            return False

    @classmethod
    def erase(cls, pk, request):
        try:
            pp_delete = cls.current(pk, request.user)
            pp_delete.delete = True
            pp_delete.save()
            return True
        except:
            return False
