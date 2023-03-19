from django.contrib import admin
from .models import Pizza, Size, Crust, Customer, Customer_Name, Customer_Email

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Crust)
admin.site.register(Customer)
admin.site.register(Customer_Name)
admin.site.register(Customer_Email)
