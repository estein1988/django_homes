from django.urls import path, include
from rest_framework import routers

from .views import HomeView

router = routers.DefaultRouter()
router.register('homes', HomeView)

urlpatterns = [
    path('', include(router.urls))
]