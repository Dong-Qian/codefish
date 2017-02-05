from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from article.models import Article
from .forms import ArticleForm


# Create your views here.
# this returns the whole article list back to the html
def home(request):
    try:
        queryset = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    paginator = Paginator(queryset, 5)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        post_list = paginator.page(paginator.num_pages)

    context = {
        'post_list': post_list,
        'post_count': len(post_list)
    }
    return render(request, 'home.html', context)

# return the single post with the detial
def postDetail(request, slug):
    try:
        postDetail = Article.objects.get(slug =slug)
        postDetail.views += 1
        postDetail.save()
    except Article.DoesNotExist:
        raise Http404
    context = {
        'postDetail': postDetail
    }

    return render(request, 'postDetail.html', context)


# return about page
def about(request):
    return render(request, 'about.html')


# return list of post according to the specific category
def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact=tag)
    except Article.DoesNotExist:
        raise Http404
    context = {
        'post_list': post_list,
    }
    return render(request, 'postList.html', context)


# return list of post according to the specific title
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
                return render(request, 'postList.html', contextYes)
            else:
                contextNo = {
                    'post_list': post_list,
                    'error': False
                }
                return render(request, 'postList.html', contextNo)

    return redirect('/')


@login_required
def post_create(request):
    form = ArticleForm(request.POST or None)

    if form.is_valid():
        instance =  form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())


    context = {
        "form": form,
    }

    return render(request, "post_form.html", context)

@login_required
def post_update(request, slug = None):
    try:
        postDetail = Article.objects.get(slug =slug)
    except Article.DoesNotExist:
        raise Http404

    form = ArticleForm(request.POST or None , instance=postDetail)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'postDetail': postDetail,
        "form": form
    }

    return render(request, 'post_form.html', context)

@login_required
def post_delete(request, slug = None):
    try:
        instance = Article.objects.get(slug =slug)
        instance.delete()
    except Article.DoesNotExist:
        raise Http404
    return HttpResponseRedirect(reverse('home'))