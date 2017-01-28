from django.http import Http404
from django.shortcuts import render, redirect
from article.models import Article


# Create your views here.
def home(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    context = {
        'post_list': post_list
    }
    return render(request, 'home.html', context)


def detail(request, slug):
    try:
        post = Article.objects.get(slug =slug)
    except Article.DoesNotExist:
        raise Http404
    context = {
        'post': post
    }


    return render(request, 'post.html', context)


def allposts(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    context = {
        'post_list': post_list,
        'error': False
    }
    return render(request, 'allposts.html', context)


def about(request):
    return render(request, 'about.html')


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    context = {
        'post_list': post_list
    }
    return render(request, 'search_tag.html', context)



def search_post(request):
    if 'search' in request.GET:
        search = request.GET['search']
        if not search:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=search)
            if len(post_list) == 0:
                contextYes={
                    'post_list': post_list,
                    'error': True
                }
                return render(request, 'allposts.html', contextYes)
            else:
                contextNo = {
                    'post_list': post_list,
                    'error': False
                }
                return render(request, 'allposts.html', contextNo)

    return redirect('/')
