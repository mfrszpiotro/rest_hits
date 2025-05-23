from rest_framework import generics
from .models import Hit
from .serializers import HitSerializer


class HitListCreateView(generics.ListCreateAPIView):
    queryset = Hit.objects.all().order_by("-created_at")[:20]
    serializer_class = HitSerializer


class HitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hit.objects.all()
    serializer_class = HitSerializer
    lookup_field = "title_url"
