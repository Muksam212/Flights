from django.db import models

# Create your models here.
class Airport(models.Model):
	code = models.CharField(max_length = 4)
	city = models.CharField(max_length = 64)

	def __str__(self):
		return f"{self.code} {self.city}"
	#1 airport consists of many flight.
	# it has the relationship of 1 to many fields

class Flight(models.Model):
	origin = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name ="departures")
	destination = models.ForeignKey(Airport, on_delete = models.CASCADE, related_name ="arrivals")
	duration = models.IntegerField()

	def __str__(self):
		return f"{self.id} - {self.origin} to {self.destination}"


class Passenger(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 64)
	flights = models.ManyToManyField(Flight, blank = True, 
		related_name = 'passengers')

	#1 Flight consists of many passengers and many passengers takes many flight. so it has the relationship betwenn
	# many to many fields

	def __str__(self):
		return f"{self.first_name} - {self.last_name}"