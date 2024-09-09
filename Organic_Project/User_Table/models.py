from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField  # Import ArrayField

class CustomUser(AbstractUser):
    profile = models.ImageField(upload_to='profiles/', null=True, blank=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    first_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    
    cart_product_ids = ArrayField(
        models.IntegerField(),  
        blank=True,
        default=list  
    )
    quantities = ArrayField(
        models.IntegerField(),
        blank=True,
        default=list
    )

    def __str__(self):
        return self.email
