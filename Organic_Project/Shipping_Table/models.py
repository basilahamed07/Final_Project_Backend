from typing import Iterable
from django.db import models

import random
# Create your models here.


class Shipping_Table(models.Model):
    PENDING = 'P'

    DELIVERED = 'D'


    SHIPPING_STATUS_CHOICES = [
        (PENDING, 'Pending'),

        (DELIVERED, 'Delivered'),

    ]
    
    Shipping_id = models.CharField(max_length=20, editable=True)
    shipping_status = models.CharField(
        max_length=1,
        choices=SHIPPING_STATUS_CHOICES,
        default=PENDING,
    )
    tracking_id = models.CharField(max_length=20,editable=True)
    
    
    
    def save(self, *awrg, **kwarg):
        collections = ["1","2","3","4","5","6","7","8","9","0"]
        code_tracking = ""
        for trash in range(10):
            code_tracking += random.choice(collections)
        self.tracking_id= code_tracking
        code_shipping = ""
        for trash in range(10):
            code_shipping += random.choice(collections)
        self.Shipping_id= code_shipping
        return super().save(*awrg, **kwarg)
