from django.db import models

# Create your models here.

class Flight(models.Model):
    airline=models.CharField(max_length=20)
    flight_number=models.CharField(max_length=10)
    departure_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    price=models.BigIntegerField()
    # price = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2)
    fee = models.IntegerField()
    travelType = models.CharField(max_length=10)
    stopAmount = models.PositiveIntegerField(default=0)
    #! burada 0 olmasi sorun olabilir dikkat
    stopPlace = models.CharField(max_length=100, blank=True, null=True)
    stopDuration = models.DurationField(blank=True, null=True)
    #! durationField dikkat

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
    #passenger=models.ManyToManyField(Passenger, related_name="reservation")       #!manytomanyField extra tablo olusturur. db e bak
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.passenger} - {self.flight}"


