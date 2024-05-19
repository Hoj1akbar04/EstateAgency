
from django.contrib import admin
from .models import Travel
from import_export.admin import ImportExportModelAdmin


@admin.register(Travel)
class TravelAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'country')
    list_display_links = ('name', 'description', 'country')
    search_fields = ('name', 'description', 'country')
    ordering = ('name',)