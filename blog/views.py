from django.shortcuts import render, get_list_or_404
from .models import BlogPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.


def index(request):
    objects = get_list_or_404(BlogPost)
    page = request.GET.get('page', 1)

    paginator = Paginator(objects, 3)

    try:
        blog_posts = paginator.page(page)
    except EmptyPage:
        blog_posts = paginator.page(paginator.num_pages)
    except:
        blog_posts = paginator.page(1)

    context = {
        'blog_posts': blog_posts
    }
    
    return render(request, 'blog/bloglist.html', context=context)
