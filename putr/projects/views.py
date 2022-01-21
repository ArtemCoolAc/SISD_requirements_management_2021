from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
import requests
from django.utils import timezone
from .models import Projects
from .forms import ProjectsForm
import json


def index(request):
    if request.user.is_authenticated:
        projects = Projects.objects.all()
        return render(request, 'projects/index.html', {'projects': projects})
    else:
        return render(request, 'authorization/login.html')


class ProjectsDetailView(DetailView):
    model = Projects
    template_name = 'projects/detail_view.html'
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class ProjectsUpdateView(UpdateView):
    model = Projects
    template_name = 'projects/update.html'
    form_class = ProjectsForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class ProjectsDeleteView(DeleteView):
    model = Projects
    success_url = 'projects/'
    template_name = 'projects/delete.html'
    context_object_name = 'project'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


def getProjects(request):
    if request.user.is_authenticated:
        projects_system_ip = 'http://127.0.0.1'
        projects_port = '8000'
        api_signin = '/api/auth/signin'
        api_get_projects = '/api/project/all'
        credentials = json.dumps({'username': 'admin', 'password': 'admin'})
        response = requests.post(f"{projects_system_ip}:{projects_port}{api_signin}",
                                 data=credentials,
                                 headers={'Content-Type': 'application/json'})
        access_token = json.loads(response.text)['accessToken']
        response = requests.get(f"{projects_system_ip}:{projects_port}{api_get_projects}",
                                headers={'Authorization': f'Bearer {access_token}'})
        projects = json.loads(response.text)
        for project in projects:
            p, updated = Projects.objects.update_or_create(id=project['id'], defaults=
            {
                'id': project['id'],
                'name': project['name'],
                'description': project['description']
            })
            p.save()
        return redirect('projects_home')
    else:
        return render(request, 'authorization/login.html')


def create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = ProjectsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('projects_home')
            else:
                error = 'Форма была неверной'
        form = ProjectsForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'projects/create.html', data)
    else:
        return render(request, 'authorization/login.html')
