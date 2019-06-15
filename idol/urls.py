# -*- coding: utf-8 -*-
from django.urls import path
from idol import views

urlpatterns = [
    path('<int:idol_id>', views.show),
    path('<int:idol_id>/', views.show),
    path('<str:size>/<int:idol_id>', views.show),
    path('<str:size>/<int:idol_id>/', views.show),
]
