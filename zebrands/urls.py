from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stockmanager/', include('stockmanager.api.urls'), name='stockmanager_api'),
]
