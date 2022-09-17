from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('price/', include('api_price.urls')),
    path('banner/', include('api_banner.urls')),
    path('news/', include('api_news.urls')),
    path('mentor/', include('mentor_api.urls')),
    path('requests/', include('api_requests.urls')),
]

