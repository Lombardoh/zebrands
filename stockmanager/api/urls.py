from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from stockmanager.api.views import ProductViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)

urlpatterns = [
  path("", include(router.urls)),
]

