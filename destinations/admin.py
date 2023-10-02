from django.contrib import admin
from .models import Destinations

@admin.register(Destinations)
class DestinationsAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'slug']
    search_fields = ['name', 'location']
    prepopulated_fields = {'slug': ('name',)}
