from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='requirements_home'),
    path('create/', views.create, name='requirements_create'),
    path('<int:pk>', views.RequirementsDetailView.as_view(), name='requirements_detail'),
    path('<int:pk>/update', views.RequirementsUpdateView.as_view(), name='requirements_update'),
    path('<int:pk>/delete', views.RequirementsDeleteView.as_view(), name='requirements_delete'),
]
