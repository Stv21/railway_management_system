import os
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
import requests
import pandas as pd
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.conf import settings
from .models import Station
from .models import Train, Ticket
import random
from core.forms import TicketBookingForm


# Create your views here.



def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login")
    stations = Station.objects.all()
    return render(request, 'index.html', {'stations': stations})

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        user = User.objects.create_user(username=username, password=password, email=email)

        # Log in the new user
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("login")  # Redirect to the login page after successful signup

    return render(request, 'signup.html')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')


    





def logoutUser(request):
    logout(request)
    return redirect("/login")

def search_products(request):
    return HttpResponse("This is the search products view.")

def Electronics(request):
    trains = Train.objects.all()
    return render(request, 'Electronics.html', {'trains': trains})

def Fashion(request):
    return render(request, 'Fashion.html')


def Sports(request):
    return render(request, 'Sports.html')

def get_station_data(request):
    station_data = {
        "stations": [
            {"id": 1, "name": "Station A"},
            {"id": 2, "name": "Station B"},
            {"id": 3, "name": "Station C"},
            # Add more stations as needed
        ]
    }
    return JsonResponse(station_data)

def get_train_data(request):
    train_data = {
        "trains": [
            {"id": 1, "departure_station": "Station A", "destination_station": "Station B", "date": "2024-04-20"},
            {"id": 2, "departure_station": "Station B", "destination_station": "Station C", "date": "2024-04-21"},
            # Add more train data as needed
        ]
    }
    return JsonResponse(train_data)

# views.py
def get_random_train(request):
    random_train = random.choice(Train.objects.all().values())
    return JsonResponse(random_train)

def book_ticket(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_confirmation')  # Redirect to confirmation page
    else:
        form = TicketBookingForm()
    return render(request, 'book_ticket.html', {'form': form})

def get_station_and_train_data(request):
    # Fetch station and train data
    station_response = get_station_data(request)
    train_response = get_train_data(request)
    station_data = station_response.json()
    train_data = train_response.json()
    return render(request, 'book_ticket.html', {'station_data': station_data, 'train_data': train_data})



from django.shortcuts import render

def book_ticket(request):
    # Dummy data for stations
    
    station_data = {
        'stations': [
            {'id': 1, 'name': 'Station A'},
            {'id': 2, 'name': 'Station B'},
            {'id': 3, 'name': 'Station C'},
            # Add more stations as needed
        ]
    }

    return render(request, 'book_ticket.html', {'station_data': station_data})

def train_details(request):
    # Assuming you have a Train model with fields like train_title, dept_timing, dept_station, etc.
    # Retrieve a list of train objects from the database
    trains = Train.objects.all()  # This will fetch all train objects from the database

    # You can further filter the trains based on your requirements
    # Example: trains = Train.objects.filter(dept_station='BORIVALI')

    # Pass the trains data to the template
    context = {'trains': trains}
    return render(request, 'train_details.html', context)
def view_tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'view_tickets.html', {'user_tickets': user_tickets})
def book_ticket(request):
    if request.method == 'POST':
        form = TicketBookingForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user  # Associate ticket with logged-in user
            ticket.save()
            return redirect('ticket_confirmation')  # Redirect to confirmation page
    else:
        form = TicketBookingForm()
    return render(request, 'book_ticket.html', {'form': form})
    
def ticket_confirmation(request):
    # Logic for ticket confirmation goes here
    return render(request, 'ticket_confirmation.html')