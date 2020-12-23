from django.contrib import admin
from .models import Retreat

class RetreatAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'date',
        'duration',
        'description',
        'price',
        'location',
        'image',
    )

admin.site.register(Retreat, RetreatAdmin)