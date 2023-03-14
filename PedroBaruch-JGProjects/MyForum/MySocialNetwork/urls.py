from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('salvar/', views.save_post, name='save'),
] 