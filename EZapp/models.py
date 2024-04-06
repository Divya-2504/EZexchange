from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserImage(models.Model):
    Imageid =  models.AutoField(primary_key=True)
    Userid = models.ForeignKey(User,on_delete = models.CASCADE)
    Image = models.ImageField(upload_to="user-profile")

class Categories(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    Category = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Category

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    Userid = models.ForeignKey(User,on_delete = models.CASCADE)
    CategoryId = models.ForeignKey(Categories , on_delete = models.CASCADE)
    Brand = models.CharField(max_length=50,null=True,blank=True)
    Year = models.IntegerField(null=True,blank=True)
    Fuel = models.CharField(max_length=20,null=True,blank=True)
    Transmission = models.CharField(max_length=50,null=True,blank=True)
    KM_driven = models.IntegerField(null=True,blank=True)
    Title = models.CharField(max_length=70)
    Description = models.TextField()
    Price = models.IntegerField(default = 0)
    Location = models.CharField(max_length=30)
    ProductImage1 = models.ImageField(upload_to="Product-images")
    ProductImage2 = models.ImageField(upload_to="Product-images")
    ProductImage3 = models.ImageField(upload_to="Product-images")
    ProductImage4 = models.ImageField(upload_to="Product-images")
    PuserName = models.CharField(max_length=50)
    Pusermail=  models.EmailField()

    def __str__(self) -> str:
        return self.Title