from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('mapa/', views.mapa),
    path('reportes/', views.reportes)
]