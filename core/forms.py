# forms.py

from django import forms
from .models import Ticket
from .models import Train

class TicketBookingForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['departure_station', 'destination_station', 'date', 'passenger_name', 'seat_number']
class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'