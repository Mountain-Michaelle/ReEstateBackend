from django.db import models
from django.utils.timezone import now
from realtors.models import Realtors

# Create your models here.


class Images(models.Model):
    image = models.ImageField(upload_to='images/listing/')
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        
        return self.name
    
    
class Listing(models.Model):
    class SaleType(models.TextChoices):
        FOR_SALE = 'For Sale'
        FOR_RENT = 'For Rent'
        
    class HouseType(models.TextChoices):
        HOUSE = 'House'
        CONDO = 'Condo'
        TOWNHOUSE = 'Townhouse'
        
    class Status(models.TextChoices):
        DRAFT = 'draft'
        PUBLISHED = 'Published'
        
    realtor = models.ForeignKey(Realtors, on_delete=models.DO_NOTHING)
    sale_type = models.CharField(max_length=200, choices=SaleType.choices, default=SaleType.FOR_SALE)
    home_type = models.CharField(max_length=200, choices=HouseType.choices, default=HouseType.HOUSE)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=10)
    longitude = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.DecimalField(max_digits=2, decimal_places=1)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False) 
    main_image = models.ImageField(upload_to='images/listing/')
    status = models.CharField(max_length=15, choices=Status.choices)
    list_date = models.DateTimeField(default=now, blank=True)
    
    
    def __str__(self):
        return self.title