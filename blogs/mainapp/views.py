from django.shortcuts import render
from django.views.generic.list import ListView
from mainapp.models import PostBlog

# Create your views here.


class BlogListView(ListView):
    queryset = PostBlog.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'blog'

        return context

