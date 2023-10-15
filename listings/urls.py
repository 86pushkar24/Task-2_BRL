from django.urls import path
from . import views

urlpatterns = [
    #for listings and creating
    path('estate/', views.listcreate.as_view()),

    # for details of property
    path('estate/<int:pk>/', views.updateretreivedestroy.as_view()),

    #for filtering by property type
    path('estate/property_type/', views.filterproperty.as_view()),

    # for filtering by bedrooms
    path('estate/bedrooms/', views.filterbedroom.as_view()),
    
    # for cheapest n properties
    path('estate/cheapest/', views.cheap.as_view()),
]
