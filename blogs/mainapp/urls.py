from django.contrib.auth.views import LogoutView
from django.urls import re_path
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.BlogListView.as_view(), name='blog_list'),
    re_path(r'login/$', mainapp.BloggerLogin.as_view(), name='login'),
    re_path(r'register/$', mainapp.BloggerRegister.as_view(), name='register'),
    re_path(r'logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'post_create/$', mainapp.PostblogCreateView.as_view(), name='post_create'),
    re_path(r'post_update/(?P<pk>\d+)/$', mainapp.PostBlogUpdateView.as_view(), name='post_update'),
    re_path(r'post_delete/(?P<pk>\d+)/$', mainapp.PostBlogDeleteView.as_view(), name='post_delete'),


]
