from django.contrib import admin
from .models import Contacts, Banner, FormUs


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('location', 'open_hours', 'email', 'number')
    search_fields = ('location', 'open_hours', 'email', 'number')


admin.site.register(Banner)


@admin.register(FormUs)
class FormUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message')
    search_fields = ('name', 'email', 'subject', 'message')
