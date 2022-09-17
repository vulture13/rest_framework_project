from django.urls import path
from .views import MentorAPI

urlpatterns = [
    path('', MentorAPI.as_view())
]
