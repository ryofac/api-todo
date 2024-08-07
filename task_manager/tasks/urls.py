from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet

app_name = "tasks"

router = DefaultRouter()
router.register("tasks", TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
