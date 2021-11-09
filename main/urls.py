
from django.urls import path
from .views import *



urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', MyObtainTokenPairView.as_view()),
    path('create/', CreateDNAView.as_view()),
    path('edit/<int:pk>/', EditDNAView.as_view()),
    path('delete/<int:pk>/', DeleteDNAView.as_view()),
    path('check/<str:codon>/', CheckDNAView.as_view())

]