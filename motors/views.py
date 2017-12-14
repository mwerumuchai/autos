from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Vehicle,Category
from django.contrib import messages
from django.db import transaction
from django.http import Http404


def index(request):
    '''
    Function that gets a list a vehicles from a category
    '''
    category = Category.get_category()

    title = 'Jeep Categories'
    return render(request, 'index.html', {"category":category})

def logout(request):
    return render(request, 'index.html')

# VEHICLE
def vehicle(request):
    '''
    Function that gets a list of specific vehicles from a category
    '''
    vehicles = Vehicle.get_vehicles()

    return render(request, 'vehicle/vehicles.html', {"vehicles":vehicles})

def single_vehicle(request,pk):
    '''
    Function that gets a vehicle information  from a specific
    '''
    vehicles = Vehicle.get_single_vehicle(pk)

    return render(request, 'vehicle/vehicles_details.html', {"vehicles":vehicles})

# search photos
