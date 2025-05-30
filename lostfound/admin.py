from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ('title','disposition' ,'status', 'location', 'date', 'reported_by')
    list_filter = ('status', 'location', 'date')
    search_fields = ('title', 'description', 'location')

admin.site.register(Item, ItemAdmin)
