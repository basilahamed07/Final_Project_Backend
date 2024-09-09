
from django.db import models
from django.core.validators import *
import random
# from django.core.validator import min
# Create your models here.
class Coupon_Table(models.Model):
    code = models.CharField(validators=[MinLengthValidator(10),MaxLengthValidator(10)], editable=False, max_length=10)
    discount = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(90)])
    
    def save(self, *awrg, **kwarg):
        series = ["A","B","C","D","E","F","G","H","J","0","1","2","3","4","5","6","7","8","9","0"]
        code = ""
        for trash in range(10):
            code += random.choice(series)
        self.code = code
        return super().save(*awrg,**kwarg)
