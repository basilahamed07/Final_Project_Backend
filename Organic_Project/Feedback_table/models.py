from django.db import models

# Create your models here

class Feedback(models.Model):
    email = models.EmailField(max_length=20)
    message = models.TextField()
    rating = models.IntegerField()
    remarks = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.email} feedback"