from django.urls import path, include
from .views import weather, menu, image, service, test
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('weather/', weather.Weather.as_view()),
    path('menu/', menu.get_menu),
    path('menu/list/', menu.MenuList.as_view()),
    path('menu/user/', menu.UserMenu.as_view()),
    path('image/', image.ImageView.as_view()),
    path('image/list/', image.ImageListView.as_view()),
    path('stock/', service.stock),
    path('constellation/', service.Constellation.as_view()),
    path('joke/', service.joke),
    path('test/', test.test),
]
