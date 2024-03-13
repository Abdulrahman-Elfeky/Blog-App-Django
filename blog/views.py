from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from datetime import date
from . models import Post
# Create your views here.


def view_home(request):
    latest_posts = Post.objects.order_by('-data')[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def view_posts(request):
    posts = Post.objects.order_by('-data')
    return render(request, "blog/all-posts.html", {
        "posts": posts
    })


def view_post_detail(request, id):
    post = get_object_or_404(Post, slug=id)
    return render(request, "blog/post-detail.html", {
        "post": post
    })
