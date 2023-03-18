from django.contrib import admin
from .models import Pizza, Size, Crust

# Register your models here.

admin.site.register(Pizza)
admin.site.register(Size)
admin.site.register(Crust)
