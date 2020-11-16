from rest_framework import routers
from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register('movies', viewset=views.MovieList)

urlpatterns = [

    path('', include(router.urls))
]