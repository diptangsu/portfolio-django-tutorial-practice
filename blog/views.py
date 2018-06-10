from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    allblogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': allblogs})


def blog(request, blog_id):
    blogobject = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog.html', {'blog': blogobject})
