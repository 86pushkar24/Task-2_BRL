from django.db import models
from django.core.validators import MinValueValidator

class Estate(models.Model):
    title = models.CharField(max_length=175)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=4,)
    property_type = models.CharField(max_length=15, choices=[
        ('Apartment', 'Apartment'),
        ('Farm House', 'Farm House'),
        ('Home', 'Home'), 
        ('Commercial', 'Commercial'),
        ('Villa', 'Villa'),
        ('Cottage', 'Cottage'),
        ('Other', 'Other'),
    ])
    listing_type = models.CharField(max_length=10, choices=[
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    ])
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    property_id = models.AutoField(primary_key=True)

#using the MinValueValidator to ensure that price and bedrooms ki value postive rahe.