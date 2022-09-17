from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mentor


class MentorAPI(APIView):
    def get(self, request):
        mnt = Mentor.objects.all()
        return Response({'mnt': list(mnt)})
