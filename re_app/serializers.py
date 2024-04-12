from rest_framework import serializers
from .models import Images, Listing

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields = ('image', 'name')
        
        
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type',
                  'bedrooms', 'bathroom', 'price', 'sqft', 'images', 'slug', 'longitude', 'latitude', 'description',
                  'list_date', 'zip_ode')
        
        depth = 1
        
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields = '__all__'
        lookup_field = 'slug' 