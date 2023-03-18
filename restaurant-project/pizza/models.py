from django.db import models

# Create your models here.


class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Crust(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    crust = models.CharField(max_length=100, default="Regular")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
