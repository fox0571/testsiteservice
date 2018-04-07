from django.contrib import admin

# Register your models here.
from .models import Partsinv

#class TaskAdmin(admin.ModelAdmin):
#    list_display = ['number']
admin.site.register(Partsinv)
