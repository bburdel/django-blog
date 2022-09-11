from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseRedirect
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PostListView(ListView):
    template_name = 'blogging/list.html'
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    # published_queryset = Post.objects.exclude(published_date__exact=None)

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['blogging_list'] = Post.objects.exclude(published_date__exact=None)
            return context
        except Post.DoesNotExist:
            raise Http404



