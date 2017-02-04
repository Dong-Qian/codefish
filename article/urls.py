from django.conf.urls import url, include
from article import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.postDetail, name='postDetail'),
    #url(r'^postList/$', views.postList, name='postList'),
    url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'search/$', views.search_post, name='search_post'),

]