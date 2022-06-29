from django.db import models
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
    exceprt = models.CharField(max_length=150)
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


