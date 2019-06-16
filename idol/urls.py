# -*- coding: utf-8 -*-
from django.urls import path
from .views import View

urlpatterns = [
    path('<int:idol_id>', View.as_view()),
    path('<int:idol_id>/', View.as_view()),
    path('<str:size>/<int:idol_id>', View.as_view()),
    path('<str:size>/<int:idol_id>/', View.as_view()),
]
