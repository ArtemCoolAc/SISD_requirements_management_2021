from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone
from .models import Specifications
from .forms import SpecificationsForm


def index(request):
    if request.user.is_authenticated:
        specifications = Specifications.objects.all()
        return render(request, 'specifications/index.html', {'specifications': specifications})
    else:
        return render(request, 'authorization/login.html')


class SpecificationsDetailView(DetailView):
    model = Specifications
    template_name = 'specifications/detail_view.html'
    context_object_name = 'specification'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class SpecificationsUpdateView(UpdateView):
    model = Specifications
    template_name = 'specifications/update.html'
    form_class = SpecificationsForm

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


class SpecificationsDeleteView(DeleteView):
    model = Specifications
    success_url = 'specifications/'
    template_name = 'specifications/delete.html'
    context_object_name = 'specification'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


def update(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            print('')
            form = SpecificationsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                # post.creator = request.user
                # post.date_creation = timezone.now()
                # post.status = 2
                post.save()
                return redirect('specifications_home')
            else:
                error = 'Форма была неверной'
        form = SpecificationsForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'specifications/update.html', data)
    else:
        return render(request, 'authorization/login.html')


def create(request):
    if request.user.is_authenticated:
        error = ''
        if request.method == 'POST':
            form = SpecificationsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.creator = request.user
                post.date_creation = timezone.now()
                post.status = 2
                post.save()
                return redirect('specifications_home')
            else:
                error = 'Форма была неверной'
        form = SpecificationsForm()
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'specifications/create.html', data)
    else:
        return render(request, 'authorization/login.html')


def error_redirect(request, pk, pk1):
    if request.user.is_authenticated:
        return redirect('specifications_home')
    else:
        return render(request, 'authorization/login.html')
