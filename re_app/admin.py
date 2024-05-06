from django.contrib import admin
from .models import Listing, Images
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('realtor', )
    list_editable = ('status', )
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code', 'price')
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)

admin.site.register(Images)