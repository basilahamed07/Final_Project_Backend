from django.db import models
from django.core.validators import *
# importing the catagory models from ccatagory appp
from category_Table.models import *
# Create your models here.


# def author_image_file_path(instance,filename):
#     return '/'.join([str(instance.name),filename])


class Product_Table(models.Model):
    P_Name = models.CharField(max_length=100)
    P_description = models.TextField(max_length=100)
    P_Price = models.FloatField(validators=[MaxValueValidator(5000), MinValueValidator(20)])
    P_Stock = models.IntegerField(validators=[MaxValueValidator(5000), MinValueValidator(20)])
    P_Category = models.ForeignKey(Category_Table, on_delete=models.CASCADE) 
    P_Brand = models.CharField(max_length=100)
    P_image = models.ImageField(upload_to="Product_Image")