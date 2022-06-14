from django.urls import include, path
from watering.views import show_watering_status, switch_pump

urlpatterns = [
    path('', show_watering_status, name='show_watering_status'),
    path('switch_pump', switch_pump, name='switch_pump'),
]
