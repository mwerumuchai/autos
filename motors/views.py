from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Vehicle,Category,VehicleDetails
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
def vehicle(request,category_id):
    '''
    Function that gets a list of specific vehicles from a category
    '''

    vehicles = Vehicle.objects.filter(category=category_id)

    return render(request, 'vehicle/vehicles.html', {"vehicles":vehicles})


def vehicledetails(request,vehicle_id):
    '''
    Functions that gets details of a specific vehicle
    '''

    vehicledetails = VehicleDetails.objects.filter(vehicle=vehicle_id)

    return render(request, 'vehicle/vehicles_details.html', {"vehicledetails":vehicledetails})

def single_vehicle(request,vehicle_id):
    '''
    Function that gets a vehicle information  from a specific type of vehicle
    '''
    try:
        # vehicles = Vehicle.objects.filter(category=category_id)
        vehicledetails = VehicleDetails.objects.get(vehicle=vehicle_id)
        print('vehicledetails')
    except VehicleDetails.DoesNotExist:
        raise Http404("The Post does not exist")

    return render(request,'vehicle/vehicle_details.html',{"vehicledetails":vehicledetails})


# search photos
def search_results(request):
    '''
    Function that gets all the searched vehicle by name
    '''

    if 'motors' in request.GET and request.GET["motors"]:
        search_term = request.GET.get("motors")
        searched_vehicles = Vehicle.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"searched_vehicles": searched_vehicles})
    else:
        message = "No Vehicles searched"
        title = 'Search Results'
        return render(request, 'search.html',{"message":message})
