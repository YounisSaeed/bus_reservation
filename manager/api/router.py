
from django.urls import path
from .viewsets import TriptList,TripDetail
urlpatterns=[
    path('trips/',TriptList.as_view()),
    path('trips/<int:pk>',TripDetail.as_view()),
]

# in your project urls import this urlss