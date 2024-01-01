from django.db import models


class Flight(models.Model):
    airline=models.CharField(max_length=20)
    flight_number=models.CharField(max_length=10)
    departure_time=models.TimeField()
    arrival_time=models.TimeField()
    price=models.BigIntegerField()
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.IntegerField()
    travel_type = models.CharField(max_length=10)
    stop_amount = models.PositiveIntegerField(default=0)
    stop_place = models.CharField(max_length=100, blank=True, null=True)
    stop_duration = models.DurationField(blank=True, null=True)

    def __str__(self):
        return f"{self.airline} - {self.flight_number}"
    


class Passenger(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"
    
    
class Reservation(models.Model):
    passenger=models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger} - {self.flight}"


