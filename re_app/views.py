from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from datetime import datetime, timezone, timedelta
from .models import Listing, Images
from .serializers import ListingSerializer, DetailSerializer, ImageSerializer


# Create your views here.
class ListingsView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Listing.objects.order_by('-list_date').filter(status=Listing.Status.PUBLISHED)
    serializer_class = ListingSerializer
    lookup_field = 'slug'
    
class ListDetails(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    queryset = Listing.objects.order_by('-list_date').filter(status=Listing.Status.PUBLISHED)
    serializer_class = ListingSerializer
    lookup_field = 'slug'
    
class ImageListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ImageSerializer
    paginator = PageNumberPagination()
    paginator.page_size = 4
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        post_slug = Listing.objects.get(slug=slug)
        return Images.objects.filter(listing=post_slug)
        

class HomePageSearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ListingSerializer
    
    def post(self, request, format=None):
        queryset = Listing.objects.order_by('-list_date').filter(status=Listing.Status.PUBLISHED)
        data = self.request.data
        min_price = data['min_price'].strip()
        max_price = data['max_price'].strip()
        city = data['city'].strip()
        sale_type = data['sale_type']
        
        paginator = PageNumberPagination()
        paginator.page_size = 3

        
        queryset = queryset.filter(sale_type__iexact=sale_type)
        
        # listing = queryset.filter(sale_type)
        print("See ", )
        
        queryset = queryset.filter(state__iexact=city)
            
        if min_price is not None and not min_price.isdigit():
            queryset = queryset.filter(price__gte=min_price)

        if max_price is not None and max_price.isdigit():
            queryset = queryset.filter(price__lte=max_price)
            
        if not queryset.exists():
            return Response({'error': 'No search result matches your filters'})

        paginated_queryset = paginator.paginate_queryset(queryset, request)
        
        serializer = ListingSerializer(paginated_queryset, many=True)
        
        
        return paginator.get_paginated_response(serializer.data)

        
class ListingPageSearchView(APIView):
        permission_classes = (permissions.AllowAny)
        def post(self, request, format=None):
            
            queryset = Listing.objects.order_by('-listing_date').filter(status=Listing.Status.PUBLISHED)
            data = self.request.data
            
            bedroom = data['bedroom']
            bathroom = data['bathroom']
            home_type = data['home_type']
            days_passed = data['days_passed']
            price = data['price']
            sqft = data['sqft']
            open_house =  data['open_house']
            keywords = data['keywords']

            if price  == '$0+':
                price = 0
                
            elif price == '$200,000':
                price =200000
            
            elif price == '$400,000':
                price = 400000
                
            elif price == '$800,000':
                price = 800000
                
            elif price == '$900,000':
                price = 900000
                
            elif price == '$1000,0000':
                price =200000
                
            elif price == '$1,200,000':
                price =1200000
                
            elif price == '$1, 500,000':
                price =1500000
            
            elif price == 'Any':
                price = -1
                
            if price != -1:
                queryset = queryset.filter(price__gte=price)
                
                
            if bedroom == '0+':
                bedroom = 0
                
            elif bedroom == '1+':
                bedroom = 1
                
            elif bedroom == '2+':
                bedroom = 2
                
            elif bedroom == '3+':
                bedroom = 3
                
            elif bedroom == '4+':
                bedroom = 4
            
            elif bedroom == '5+':
                bedroom = 5
            
            
            queryset = queryset.filter(bedroom__gte=bedroom)
            queryset = queryset.filter(home_type__iexact=home_type)
            
            if bathroom == '0+':
                bathroom = 0.0
            
            elif bathroom == '1+':
                bathroom = 1.0
                
            elif bathroom == '2+':
                bathroom = 2.0
                
            elif bathroom == '3+':
                bathroom = 3.0
                
            elif bathroom == '4+':
                bathroom = 4.0
                
            queryset = queryset.filter(bathroom__gte=bathroom)
            
            if sqft == '1000+':
                sqft = 1000
                
            elif sqft == '1200':
                sqft = 1200
            
            elif sqft == '1400':
                sqft = 1400
                
            elif sqft == '1800':
                sqft = 1800
            
            elif sqft == '1900':
                sqft = 1900
            
            elif sqft == '2000':
                sqft = 2000
            
            elif sqft != 0:
                queryset = queryset.filter(sqft__gte=sqft)
            
            
            if days_passed == '1 or less':
                days_passed = 1
            
            elif days_passed == '2 or less':
                days_passed = 2
            
            elif days_passed == '5 or less':
                days_passed = 5
            
            elif days_passed == '10 or less':
                days_passed = 10
            
            elif days_passed == '20 or less':
                days_passed = 20
            
            elif days_passed == '2 or less':
                days_passed = 2
                
            for query in queryset:
                num_days = (datetime.now(timezone.utc) - query.list_date).days
                
                if days_passed != 0:
                    if num_days > days_passed:
                        slug=query.slug
                        queryset = queryset.exclude(slug__iexact=slug)
                        
            
            queryset = queryset.filter(open_house__iexact=open_house)
            
            queryset = queryset.filter(description__iexact=keywords)
            serializer = ListingSerializer(queryset, many=True)
            
            if not queryset.exists():
                return Response({'error': 'No result matches your search'})
            else:
                return Response(serializer.data)