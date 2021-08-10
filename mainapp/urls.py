from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.example),
    path('sapa/<str:nama>/',views.sapa),
    path('count/<int:angka>/',views.count),
    path('second/', views.second_page),
    path('', views.landing_page),
]