from django.contrib import admin

from home.models import Contact

# Register your models here
admin.site.register(Contact)

from .models import CarbonFootprint

admin.site.register(CarbonFootprint)