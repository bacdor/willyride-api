from rest_framework import viewsets
from .models import User, RideRequest, RideOffer
from .serializers import UserSerializer, RideRequestSerializer, RideOfferSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequest.objects.all()
    serializer_class = RideRequestSerializer

class RideOfferViewSet(viewsets.ModelViewSet):
    queryset = RideOffer.objects.all()
    serializer_class = RideOfferSerializer
