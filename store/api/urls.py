from django.urls import path, include

from api.views import ProductModelViewSet
from rest_framework import routers
from django.views.decorators.cache import cache_page

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
