from django.db import models
from django.contrib.postgres.fields import ArrayField
from User_Table.models import CustomUser
from Product_Table.models import Product_Table
from Shipping_Table.models import Shipping_Table

class Order_table(models.Model):
    user_id = models.IntegerField(default=0)
    shipping = models.IntegerField(default=0)
    order_date = models.DateField(auto_now=True)
    product_ids = ArrayField(models.IntegerField(), blank=True, default=list)
    quantity = ArrayField(models.IntegerField(default=1), blank=True, default=list) 
    total_price = models.IntegerField(default=0)

    def __str__(self):
        return f"Order {self.id} by {self.user_id}" 
