from django.db import models
from autoslug import AutoSlugField
from core.user import User


class SocialNetwork(models.Model):
    """social network"""

    TYPE_PROFILE = ((1, "professional-profile"), (2, "profile-company"))
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from="name", always_update=True)
    profile = models.PositiveSmallIntegerField(choices=TYPE_PROFILE, default=0)
    delete = models.BooleanField(default=False)
    link = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.name

    @classmethod
    def list(cls, request): 
        all = cls.objects.filter(
            profile=request.query_params.get("profile"),
            user=request.user,
            delete=False
        )
        return all

    @classmethod
    def current(cls, pk, request, delete=False):
        actual = cls.objects.get(
            id=pk,
            profile=request.query_params.get("profile"), 
            user=request.user,
            delete=delete
        )
        return actual

    @classmethod
    def create(cls, request):
        try:
            created = cls.objects.create(
                name=request.data.get("name"),
                link=request.data.get("link"),
                profile=request.data.get("profile"),
                user=request.user
            )
            return created.id
        except Exception as e:
            return e

    @classmethod
    def update(cls, pk, request):
        try:
            single = cls.current(pk, request)
            single.name = request.data.get("name")
            single.link = request.data.get("link")
            single.save()
            return True
        except:
            return False

    @classmethod
    def erase(cls, pk, request):
        try:
            deleted = cls.current(pk, request)
            deleted.delete = True
            deleted.save()
            return True
        except:
            return False
