from django.shortcuts import render
from .serializers import Flight,Passenger,Reservation,FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
# Create your views here.


class FlightView(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

class PassengerView(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationView(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer


