
from django.contrib import admin
from .models import Comments, City, Address, Users, Country, Testimonials, Agency, Agents
from import_export.admin import ImportExportModelAdmin


@admin.register(Testimonials)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ('id', 'content', 'image', 'client_name')
    list_display_links = ('id', 'content', 'image', 'client_name')
    search_fields = ('id', 'content', 'client_name')
    ordering = ('content',)


@admin.register(City)
class CityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    search_fields = ('id', 'name')
    ordering = ('name',)


@admin.register(Comments)
class CommentsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'comment', 'create_date')
    list_display_links = ('id', 'comment', 'create_date')
    ordering = ('id',)
    search_fields = ('comment',)


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    search_fields = ('id', 'name')
    ordering = ('id',)


@admin.register(Address)
class AddressAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_update')
    list_display_links = ('id', 'name', 'last_update')
    search_fields = ('id', 'name')
    ordering = ('id',)


@admin.register(Users)
class UsersAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'username', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'username', 'phone_number')
    search_fields = ('id', 'first_name', 'last_name')
    ordering = ('first_name',)


@admin.register(Agency)
class AgencyAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name', 'address')
    search_fields = ('id', 'name')
    ordering = ('name', )


@admin.register(Agents)
class AgentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    list_display_links = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('id', 'first_name', 'last_name', 'email')
    ordering = ('first_name',)
