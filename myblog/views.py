from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def showblog(request):
    posts = Blog.objects
    return render(request, 'blog/blog.html', {'posts': posts})

def specific_post(request, post_id):
    post = get_object_or_404(Blog, pk=post_id)
    return render(request, 'blog/specific_post.html', {'post': post})