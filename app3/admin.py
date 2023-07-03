from django.contrib import admin
from .models import Fram_dt
# Register your models here.

@admin.register(Fram_dt)
class AdFram(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'email', 'gender', 'region', 'stype', 'subtp', 'nextcrop']
