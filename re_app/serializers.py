from rest_framework import serializers
from .models import Images, Listing

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields = '__all__'
        lookup_field = 'slug'
        
        
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type',
                  'bedroom', 'bathroom', 'price', 'sqft', 'main_image', 'slug', 'longitude', 'latitude', 'description',
                  'list_date', 'zip_code')
        
        depth = 1
        
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Images
        fields = '__all__'
        lookup_field = 'slug' 