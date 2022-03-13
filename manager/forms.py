from dataclasses import field
from .models import Trip
from django import forms
from passanger.models import Book
class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['company_name','dest_from','dest_to','time_from','time_to','date_day','price']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['author','recet_number','trip_id','status']