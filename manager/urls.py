from django.urls import path , include
from .views import list_trips,delete_trip,trip_details,create_trip,edit_trip,search_recet,change_status
urlpatterns = [
    path('create/',create_trip,name='create'),
    path('list/',list_trips,name='manager_list'),
    path('edit/<int:id>',edit_trip,name='edit'),
    path('delete/<int:id>',delete_trip,name='delete'),
    path('details/<int:id>',trip_details,name='detail'),
    path('search-number',search_recet,name='searcher'),
    path('Book_status/<int:id>',change_status,name='status'),
    
    
]