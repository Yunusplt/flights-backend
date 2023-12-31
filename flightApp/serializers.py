from rest_framework import serializers
from .models import Flight, Passenger, Reservation


class FlightSerializer(serializers.ModelSerializer):
    # duration = serializers.SerializerMethodField()         #! hocaya sor.... 
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields="__all__"     #! bu kisma duration eklemelimiyim???
    
    def get_total_price(self,obj):
        return round((obj.price * obj.tax) + obj.fee)




class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields="__all__"


class ReservationSerializer(serializers.ModelSerializer):
    flight= serializers.StringRelatedField()           
    flight_id=serializers.StringRelatedField()
    #! yukaridakileri ekleyince asagida sadece __all__ yeterli olmuyor sanirim 
    passenger = PassengerSerializer(many=True)

    class Meta:
        model = Reservation
        fields="__all__"

