from django.db import models
from django.core.validators import MinValueValidator

class Estate(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,)
    property_type = models.CharField(max_length=20, choices=[
        ('Apartment', 'Apartment'),
        ('Home', 'Home'),
        ('Cottage', 'Cottage'),
        ('Farm House', 'Farm House'),
    ])
    listing_type = models.CharField(max_length=10, choices=[
        ('Rent', 'Rent'),
        ('Sale', 'Sale'),
    ])
    bedrooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    property_id = models.AutoField(primary_key=True)

#using the MinValueValidator to ensure that price and bedrooms are good values.