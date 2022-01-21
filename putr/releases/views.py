from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from django.utils import timezone
from .models import Releases
from .forms import ReleasesForm


def index(request):
    if request.user.is_authenticated:
        releases = Releases.objects.all()
        return render(request, 'releases/index.html', {'releases': releases})
    else:
        return render(request, 'authorization/login.html')


class ReleasesDetailView(DetailView):
    model = Releases
    template_name = 'releases/detail_view.html'
    context_object_name = 'release'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return render(request, 'authorization/login.html')


class ReleasesUpdateView(UpdateView):
    model = Releases
    template_name = 'releases/update.html'
    form_class = ReleasesForm

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


class ReleasesDeleteView(DeleteView):
    model = Releases
    success_url = 'releases/'
    template_name = 'releases/delete.html'
    context_object_name = 'release'

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
            form = ReleasesForm(request.POST, user=request.user)
            if form.is_valid():
                post = form.save(commit=False)
                post.creator = request.user
                post.save()
                return redirect('releases_home')
            else:
                error = 'Форма была неверной'
        form = ReleasesForm(user=request.user)
        data = {
            'form': form,
            'error': error
        }
        return render(request, 'releases/create.html', data)
    else:
        return render(request, 'authorization/login.html')
