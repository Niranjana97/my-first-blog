# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post
from .models import Personal
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'blog/post_list.html'
# def post_list(request):
#     posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})


class List(ListView):
    template_name = 'blog/post.html'
    model = Post


class Detailed(DetailView):
    template_name = 'blog/new.html'
    model = Post


class List2(ListView):
    template_name = 'blog/user.html'
    model = Personal


class Detail2(DetailView):
    template_name = 'blog/detail.html'
    model = Personal


class Delete(DeleteView):
    template_name = 'blog/del.html'
    model = Post