from django.urls import path
from .views import PriceAPIView


urlpatterns = [
    path('', PriceAPIView.as_view())
]