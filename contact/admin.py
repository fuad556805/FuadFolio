from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')   # model এ subject নেই, তাই name/email/sent_at
    list_filter = ('sent_at',)
    search_fields = ('name', 'email', 'message')
