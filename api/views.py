from django.shortcuts import render
from rest_framework import viewsets

from .models import TrashCan, TrashState
from .serializers import TrashCanSerializer, TrashStateSerializer

class TrashCanViewSet(viewsets.ModelViewSet):
    queryset = TrashCan.objects.all()
    serializer_class = TrashCanSerializer

class TrashStateViewSet(viewsets.ModelViewSet):
    queryset = TrashState.objects.all()
    serializer_class = TrashStateSerializer