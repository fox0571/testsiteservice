from django.contrib import admin
from .models import Address, Person, Part, Request
# Register your models here.
admin.site.register(Request)
admin.site.register(Address)
admin.site.register(Person)
admin.site.register(Part)
