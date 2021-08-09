from django.contrib import admin
from .models import CSVObject


@admin.register(CSVObject)
class CSVObjectDisplay(admin.ModelAdmin):
    list_display = [field.name for field in CSVObject._meta.get_fields()]
    search_fields = ('code',)
