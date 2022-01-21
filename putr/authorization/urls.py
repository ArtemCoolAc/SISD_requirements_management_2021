from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login, name='authorization_home'),
    path('logout/', views.logout),
]
