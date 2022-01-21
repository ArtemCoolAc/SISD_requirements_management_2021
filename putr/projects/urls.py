from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='projects_home'),
    path('create/', views.create, name='projects_create'),
    path('<int:pk>', views.ProjectsDetailView.as_view(), name='projects_detail'),
    path('<int:pk>/update', views.ProjectsUpdateView.as_view(), name='projects_update'),
    path('<int:pk>/delete', views.ProjectsDeleteView.as_view(), name='projects_delete'),
    path('get_projects/', views.getProjects, name='get_projects'),
]
