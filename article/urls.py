from django.conf.urls import url, include
from article import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<slug>[-\w]+)/$', views.postDetail, name='postDetail'),
    url(r'^post/(?P<slug>[-\w]+)/edit/$', views.post_update, name='post_update'),
    url(r'^post/(?P<slug>[-\w]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^about/$', views.about, name='about'),
    url(r'^game/space_ship$', views.space_ship, name='space_ship'),
    url(r'^category/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.search_post, name='search_post'),
    url(r'^create/$', views.post_create, name='post_create')
]