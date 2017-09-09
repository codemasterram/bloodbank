from django.contrib import admin


# Register your models here.
from .models import Bloodbank,Donors

admin.site.register(Bloodbank)
admin.site.register(Donors)

