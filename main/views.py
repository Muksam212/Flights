from django.shortcuts import render, get_object_or_404, reverse
from django.http import Http404, HttpResponse
from .models import Flight, Passenger
# Create your views here.

def homepage(request):
	return render(request,'main/index.html',context={'flights':Flight.objects.all()})


def flight(request, id):
	flight = get_object_or_404(Flight, pk = id) #ki ta malae object de ki ta 404 error de bhaneko ho get_object_or_404
	passengers = flight.passengers.all() #since flight and passenger have many to many fields
	context ={'flights':flight,'passengers':passengers}
	return render(request,'main/flight.html', context)

def book(request, id):
	passenger_id = request.POST["passengers"]
	flight = Flight.objects.get(pk = id)
	passenger = Passenger.objects.get(pk = passenger_id)

	passenger.flights.add(flight) #Manytomany field huda kasari value add garne bhaneko ho

	return HttpResponse("Passenger is added")