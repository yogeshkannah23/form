from django.db import models

# Create your models here.
class Login(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name +" "+  self.last_name