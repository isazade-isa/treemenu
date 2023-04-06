from django.urls import path
from . import views

urlpatterns = [
    path('draw_menu/', views.draw_menu, name='draw_menu'),
]
