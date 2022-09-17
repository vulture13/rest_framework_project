from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Request_api
from django.forms import model_to_dict

class RequestView(APIView):
    def post(self, request):
        post_new = Request_api.objects.create(
            name=request.data['name'],
            number_phone=request.data['number_phone']
        )
        return Response({'post': model_to_dict(post_new)})
