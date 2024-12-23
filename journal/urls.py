from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('profile/', views.profile, name='profile'),
]
