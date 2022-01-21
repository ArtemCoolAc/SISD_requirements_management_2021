from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib import auth
from .models import Requirements
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import RequirementsForm


def index(request):
    if request.user.is_authenticated:
        requirements = Requirements.objects.all()
        return render(request, 'requirements/index.html', {'requirements': requirements})
    else:
        return render(request, 'authorization/login.html')


class RequirementsDetailView(DetailView):
    model = Requirements
    template_name = 'requirements/detail_view.html'
    context_object_name = 'requirement'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class RequirementsUpdateView(UpdateView):
    model = Requirements
    template_name = 'requirements/update.html'
    form_class = RequirementsForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            form_class = self.get_form_class()
            form = self.get_form(form_class)
            form.update_block_form(user=request.user, action='update')
            context = self.get_context_data(object=self.object)
            context['form'] = form
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class RequirementsDeleteView(DeleteView):
    model = Requirements
    success_url = 'requirements/'
    template_name = 'requirements/delete.html'
    context_object_name = 'requirement'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


def create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = RequirementsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.creator = request.user
                post.date_creation = timezone.now()
                post.status = 1
                post.save()
                return redirect('requirements_home')
            else:
                error = 'Форма была неверной'
        form = RequirementsForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'requirements/create.html', data)
    else:
        return render(request, 'authorization/login.html')
