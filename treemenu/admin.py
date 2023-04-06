from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'url')
    list_filter = ('parent',)


admin.site.register(MenuItem, MenuItemAdmin)
