from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'AddtaskViewSet', views.AddtaskViewSet)

urlpatterns = [
    path('', views.todoBoard),
    path('todoBoard/', include(router.urls)),
]
