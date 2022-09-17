from .models import Images_api
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import ListView


class ImageAPI(ListView):
    def get(self, request):
        img = Images_api
        return Response(list(img))

