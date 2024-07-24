from django.contrib import admin
from .models import Cars



class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'year')

admin.site.register(Cars,CarAdmin)

