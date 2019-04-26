from django.http import HttpResponse, JsonResponse
from django.urls import path, include

urlpatterns = [
    path('service/', include('apis.urls')),
    path('auth/', include('authorization.urls')),
]
