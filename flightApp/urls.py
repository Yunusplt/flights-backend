from django.urls import path,include
#!modelViewSet kullandigimiz icin view de. 
from rest_framework.routers import DefaultRouter 
from .views import FlightView,ReservationView,PassengerView

router = DefaultRouter()
router.register("flights", FlightView)
router.register("reservation",ReservationView)
router.register("passenger",PassengerView)


urlpatterns = [
    path('',include(router.urls)) 
]



