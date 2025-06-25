from django.contrib import admin
from .models import GPSData

@admin.register(GPSData)
class GPSDataAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'date', 'time', 'created_at')
    list_filter = ('date',)
    ordering = ('-created_at',)
