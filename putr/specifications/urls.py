from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='specifications_home'),
    path('create/', views.create, name='specifications_create'),
    path('<int:pk>', views.SpecificationsDetailView.as_view(), name='specifications_detail'),
    path('<int:pk>/update', views.SpecificationsUpdateView.as_view(), name='specifications_update'),
    path('<int:pk>/delete', views.SpecificationsDeleteView.as_view(), name='specifications_delete'),
    path('<int:pk>/specifications/<int:pk1>/', views.error_redirect, name='error_redirect')
]
