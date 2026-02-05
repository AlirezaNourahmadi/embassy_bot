from rest_framework import viewsets

from .models import ReservationRequest
from .serializers import ReservationRequestSerializer


class ReservationRequestViewSet(viewsets.ModelViewSet):
    queryset = ReservationRequest.objects.select_related("user").order_by("created_at")
    serializer_class = ReservationRequestSerializer
