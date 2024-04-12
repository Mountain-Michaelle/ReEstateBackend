from django.contrib import admin
from .models import ReAccountUser
# Register your models here.


class ReAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_active', 'is_staff' )
    list_display_links = ('id', 'name', )
    
admin.site.register(ReAccountUser, ReAccountAdmin)