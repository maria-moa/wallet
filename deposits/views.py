from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .exceptions import WalletAccessException
from .models import Deposit
from .serializers import DepositSerializer


class DepositCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DepositSerializer

    def get_queryset(self):
        user = self.request.user
        return Deposit.objects.filter(created_by=user)

    def perform_create(self, serializer):
        user = self.request.user
        if not serializer.validated_data["wallet"].owner_id == user.id:
            raise WalletAccessException

        serializer.save(created_by=user)
