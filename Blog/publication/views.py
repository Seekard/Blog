from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse

from .models import *
from .forms import *


def main_page(request):
    context = {
        'publications': '123',
    }
    return render(request, 'Blog/main_page.html', context)


class PublicationList(ListView):
    model = PublicationForm
    context_object_name = 'publications'
    template_name = 'Blog/publications_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Записки сумасшедшего'
        return context

    def get_queryset(self):
        return Publications.objects.all()


class SinglePublication(DetailView):
    model = Publications
    context_object_name = 'publication'
    template_name = 'Blog/publications_detail.html'


class AddPublication(LoginRequiredMixin, CreateView):
    form_class = PublicationForm
    template_name = 'Blog/AddPublication.html'
    login_url = '/admin/'




