# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Bike, Rating, Reservation, Role
from .serializers import UserSerializer, BikeSerializer, RatingSerializer, ReservationSerializer

# Create your views here.

@api_view(['GET'])
def getBikes(request):
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data)