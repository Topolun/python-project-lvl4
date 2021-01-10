from django.contrib import admin
from fcm.models import rack


# Register your models here.
class RackAdmin(admin.ModelAdmin):
    fields = ['cell_number', 'cell_is_empty']
    list_display = ('id', 'cell_number', 'stored_items_count', 'stored_items_owner', 'stored_since')
    list_filter = ['stored_since']

admin.site.register(rack, RackAdmin)
