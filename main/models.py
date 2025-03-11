from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    namemodel = models.CharField(max_length=55)
    emailmodel = models.EmailField(unique=True)
    phonemodel = PhoneNumberField(unique=True,region='NP',null=True)
    messagemodel = models.TextField()

class Category(models.Model):
    titlemodel = models.CharField(max_length=200)
    def __str__(self):
        return self.titlemodel

class Momo(models.Model):
    momoname = models.CharField(max_length=55)
    Category= models.ForeignKey(Category,on_delete=models.CASCADE) ##ondelete mathi delete huda tala ni delete hunxa
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to="momo_images")

    def __str__(self):
        return self.momoname

