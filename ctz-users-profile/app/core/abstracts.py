from django.db import models

class AbstractProfile(models.Model):
    """abtract profile"""

    address = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    cellphone = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    description = models.CharField(max_length=250)

    class Meta:
        abstract = True
    
