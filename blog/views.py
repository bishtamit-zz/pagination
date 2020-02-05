from django.shortcuts import render, get_list_or_404
from .models import BlogPost


# Create your views here.


def index(request):
    blog_posts = get_list_or_404(BlogPost)
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blog/bloglist.html', context=context)
