from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('order', 'level', 'institution', 'degree', 'period')
    list_display_links = ('institution',)
    list_editable = ('order',)
    list_filter = ('level',)
    search_fields = ('institution', 'degree', 'description')
    ordering = ('order', '-id')
