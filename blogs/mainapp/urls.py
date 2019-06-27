from django.contrib.auth.views import LogoutView
from django.urls import re_path, include
import mainapp.views as mainapp
from importlib import import_module

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', mainapp.BlogListView.as_view(), name='blog_list'),
    re_path(r'login/$', mainapp.BloggerLogin.as_view(), name='login'),
    re_path(r'register/$', mainapp.BloggerRegister.as_view(), name='register'),
    re_path(r'logout/$', LogoutView.as_view(), name='logout'),
    # re_path(r'^accounts/', (import_module('django.contrib.auth.urls'), 'accounts', 'accounts')),


]
