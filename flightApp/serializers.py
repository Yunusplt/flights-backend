from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields="__all__"   
    
    def get_total_price(self,obj):
        return round((obj.price * obj.tax) + obj.fee)
    

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields="__all__"


class ReservationSerializer(serializers.ModelSerializer):
    # flight= serializers.StringRelatedField()  
    # passenger = serializers.StringRelatedField()  
    passenger_id=serializers.IntegerField()
    passenger = PassengerSerializer(read_only=True)
    flight_id=serializers.IntegerField()  
    flight = FlightSerializer(read_only=True)
         

    class Meta:
        model = Reservation
        fields="__all__"
            
        

