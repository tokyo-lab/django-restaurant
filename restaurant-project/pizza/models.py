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


class Customer_Name(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Customer_Email(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Pizza(models.Model):
    crust = models.ForeignKey(Crust, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.ForeignKey(Customer_Name, on_delete=models.CASCADE)
    email = models.ForeignKey(Customer_Email, on_delete=models.CASCADE)
