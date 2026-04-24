from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('sent_at',)
    ordering = ('-sent_at',)
