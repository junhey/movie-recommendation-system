from django.contrib import admin

# Register your models here.
from .models import *

class FilmAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(Film,FilmAdmin)