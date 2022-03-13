from django.urls import path , include
from .views import list_trips,book_trip,trip_detial
urlpatterns = [
    path('list/',list_trips,name='list'),
    path('invoice',book_trip,name='reserve'),
    path('details/<int:id>',trip_detial,name='details'),
    
]