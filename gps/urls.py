from django.urls import path
from .views import receive_gps_data

urlpatterns = [
    path('api/gps/', receive_gps_data, name='receive_gps_data'),
]
