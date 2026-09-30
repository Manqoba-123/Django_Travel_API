from rest_framework import generics
from .models import Destination
from .serializers import DestinationSerializer

class DestinationListCreateView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
