from urllib import request, response

from django.http import Http404 
from manager.models import Trip
from .serializers import TripSerializers
from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


class TriptList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializers
    
    def get_queryset(self):
        return Trip.objects.filter(author=self.request.user)


class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializers
    ''' def get_object(self,pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:  
            raise Http404
    def delete(self,request, pk):
        rem = self.get_object(pk)
        rem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) '''
       
    #  if you want to get user trips
    #def get_queryset(self):
    #     return Trip.objects.filter(author=self.request.user)

