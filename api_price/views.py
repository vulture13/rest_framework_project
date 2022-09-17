from .models import Price_api
from rest_framework.views import APIView
from rest_framework.response import Response

class PriceAPIView(APIView):
    def get(self, request):
        price = Price_api.objects.all().values()
        return Response(list(price))
