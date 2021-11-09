from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, MyTokenObtainPairSerializer, DNASerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView) :
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class MyObtainTokenPairView(TokenObtainPairView) :
    serializer_class = MyTokenObtainPairSerializer

class CreateDNAView(generics.CreateAPIView) :
    queryset = DNA
    serializer_class = DNASerializer
    permission_classes = (IsAuthenticated, )

class EditDNAView(generics.UpdateAPIView) :
    queryset = DNA
    serializer_class = DNASerializer
    permission_classes = (IsAuthenticated, )

class DeleteDNAView(generics.DestroyAPIView) :
    queryset = DNA
    serializer_class = DNASerializer
    permission_classes = (IsAuthenticated, )

class CheckDNAView(generics.ListAPIView) :
    def get_queryset(self):
        codon = self.kwargs['codon']
        for dna in DNA.objects.all() :
            if codon in dna.chain :
                return (dna, )
    serializer_class = DNASerializer
    permission_classes = (IsAuthenticated, )

