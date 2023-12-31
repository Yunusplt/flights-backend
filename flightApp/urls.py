from django.urls import path,include
#!modelViewSet kullandigimiz icin view de. 
from rest_framework.routers import DefaultRouter 
from .views import FlightView

router = DefaultRouter()
router.register=("flights", FlightView)
urlpatterns = [
    path('',include(router.urls)) 
]



