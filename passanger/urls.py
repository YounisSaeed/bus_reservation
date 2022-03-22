from django.urls import path , include
from .views import list_trips,book_trip,trip_detial,search_dest
urlpatterns = [
    path('list/',list_trips,name='list'),
    path('invoice',book_trip,name='reserve'),
    path('details/<int:id>',trip_detial,name='details'),
    path('result',search_dest,name='SEARCH'),
    
]