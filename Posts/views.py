from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from .forms import PostsCreateForm
from .models import Posts

class PostsListView(ListView):

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        if slug:
            queryset = Posts.objects.filter(
                    Q(category__iexact=slug)|
                    Q(category__icontains=slug)
            )
        else:
            queryset = Posts.objects.all()
        return queryset

class PostsDetailView(DetailView):
    queryset = Posts.objects.all()


class PostsCreateView(CreateView):
    form_class = PostsCreateForm
    template_name = 'Posts/form.html'
    success_url = '//'

# Create your views here.
