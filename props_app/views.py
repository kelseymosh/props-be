from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import User, Plant, Favorite
from .serializers import UserSerializer, PlantSerializer, FavoriteSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny,]
    

class PlantView(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class FavoriteView(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    

class ProfileView(viewsets.ViewSet):
    queryset = User.objects.all()
    def list(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)