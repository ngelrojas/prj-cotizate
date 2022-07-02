from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from autoslug import AutoSlugField

def nameFile(instance, filename):
    fdir = str(instance).replace(" ", "_")
    return '/'.join(['images/campaings', fdir, filename])


class Campaing(models.Model):
    STATUS = ((1, "created"), (2, "draft"), (3, "send"), (4, "approve"),(5, "public"))
    FLAG = ((1, "recent"), (2,"hot"), (3, "ended"))
    profile_id = models.IntegerField()
    title = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from="title", always_update=True)
    excerpt = models.CharField(max_length=150)
    description = models.TextField()
    img_main = models.ImageField(upload_to=nameFile, blank=True, null=True)
    url_video = models.CharField(max_length=250, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=1) 
    currency_id = models.IntegerField(default=1)
    country_id = models.IntegerField(default=1)
    city_id = models.IntegerField(default=1)
    categor_ies = ArrayField(models.CharField(max_length=70)) 
    slogan_campaing = models.CharField(max_length=150)
    flag = models.PositiveSmallIntegerField(choices=FLAG, default=1)
    start_at = models.DateField(blank=True, null=True)
    ended_at = models.DateField(blank=True, null=True)
    public_at = models.DateField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)
    update_at = models.DateField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

    @classmethod
    def list(cls, request, pk):
        all = cls.objects.filter(
            profile_id=pk,
            deleted=False
        )
        return all

    @classmethod
    def current(cls, pk, request):
        actual = cls.objects.get(
            id=pk,
            profile_id = request.data.get("profile_id"),
            deleted=False
        )
        return actual

    @classmethod
    def create(cls, request):
        created = cls.objects.create(
            profile_id = request.data.get("profile_id"), 
            title = request.data.get("title"), 
            excerpt = request.data.get("excerpt"), 
            description = request.data.get("description"),
            img_main = request.data.get("img_main"), 
            url_video = request.data.get("url_video"), 
            currency_id = request.data.get("currency_id"), 
            country_id = request.data.get("country_id"), 
            city_id = request.data.get("city_id"), 
            categor_ies = request.data.get("categor_ies"), 
            slogan_campaing = request.data.get("slogan_campaing"), 
            start_at = request.data.get("start_at"), 
            ended_at = request.data.get("ended_at"), 
            created_at = datetime.now().date(), 
        )
        return created.id


    @classmethod
    def update(cls, pk, request):
        single = cls.current(pk, request)
        single.currency_id = request.data.get("currency_id")
        single.country_id = request.data.get("country_id")
        single.city_id = request.data.get("city_id")
        single.title = request.data.get("title")
        single.profile_id = request.data.get("profile_id")
        single.excerpt = request.data.get("excerpt")
        single.description = request.data.get("description")
        single.img_main = request.data.get("img_main")
        single.url_video = request.data.get("url_video")
        single.categor_ies = request.data.get("categor_ies")
        single.slogan_campaing = request.data.get("slogan_campaing")
        single.start_at = request.data.get("start_at")
        single.ended_at = request.data.get("ended_at")
        single.update_at = datetime.now().date()
        single.save()
        return True

    @classmethod
    def erase(cls, pk, request):
        deleted = cls.current(pk, request)
        deleted.deleted = True
        deleted.save()
        return True

