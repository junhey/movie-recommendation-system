from django.contrib import admin

# Register your models here.
from .models import *

class FilmAdmin(admin.ModelAdmin):
    list_display = ['id','name','brief','genres']


class GenresAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['id','user','rating','time']

class SysconfigAdmin(admin.ModelAdmin):
    list_display = ['k','random']

admin.site.register(Film,FilmAdmin)
admin.site.register(Genres,GenresAdmin)
admin.site.register(Rating,RatingAdmin)
admin.site.register(Sysconfig,SysconfigAdmin)