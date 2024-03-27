from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet, LabelViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'labels', LabelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]