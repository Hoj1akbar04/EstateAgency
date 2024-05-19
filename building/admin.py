from django.contrib import admin
from .models import Build
from import_export.admin import ImportExportModelAdmin


@admin.register(Build)
class TravelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'price', 'area', 'beds', 'baths', 'garages', 'address')
    list_display_links = ('name', 'description', 'price', 'area', 'beds', 'baths', 'garages', 'address')
    search_fields = ('name', 'description', 'price', 'area', 'beds', 'baths', 'garages', 'address')
    ordering = ('name',)