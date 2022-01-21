from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='releases_home'),
    path('create/', views.create, name='releases_create'),
    path('<int:pk>', views.ReleasesDetailView.as_view(), name='releases_detail'),
    path('<int:pk>/update', views.ReleasesUpdateView.as_view(), name='releases_update'),
    path('<int:pk>/delete', views.ReleasesDeleteView.as_view(), name='releases_delete'),
]
