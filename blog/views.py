from django.shortcuts import render
from .models import Blog


def all_blogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': allblogs})
