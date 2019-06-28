from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from mainapp.models import PostBlog, Blogger
from mainapp.forms import AdminShopUserRegisterForm

# Create your views here.
from mainapp.forms import PostblogReadForm


class BlogListView(ListView, LoginRequiredMixin):

    template_name = 'mainapp/postblog_list.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            blogs = Blogger.objects.all().values('id', 'subscription').filter(id=self.request.user.id)
            tmp_queryset = []
            for i in range(len(blogs)):
                # if len(tmp_queryset) == 0:
                tmp_queryset += PostBlog.objects.filter(blog_id=blogs[i]['subscription']).filter(readed=False)\
                    .order_by('-date')
                # else:
                #     tmp_val = PostBlog.objects.filter(blog_id=blogs[i]['subscription']).order_by('-date')
                #
                #     print(tmp_val[0].date)
                #     for j in range(len(tmp_queryset)):
                #         for s in tmp_val:
                #             if s.date > tmp_queryset[j].date:
                #                 tmp_queryset.insert(j, tmp_val)
                # print(tmp_queryset)

            self.queryset = tmp_queryset
            return self.queryset
        else:
            return None

    # class Meta:
    #     ordering = ('date',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.request.user
        return context


class BloggerRegister(CreateView):
    model = Blogger
    success_url = reverse_lazy('mainapp:login')
    form_class = AdminShopUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'create'
        return context


class BloggerLogin(LoginView):
    template_name = 'mainapp/login.html'


class PostblogCreateView(CreateView):
    model = PostBlog
    success_url = reverse_lazy('mainapp:blog_list')
    form_class = PostblogReadForm

    def send_mail(self):
        verify_link = reverse('mainapp:login')

        title = f'New Post {self.object.title}'

        message = f'To read new post {self.object.title} on the \
        {settings.DOMAIN_NAME} click on: \n{settings.DOMAIN_NAME}{verify_link}'

        # for i in :
        #     users = Blogger.objects.filter(subscription=)
        return send_mail(title, message, settings.EMAIL_HOST_USER, [self.request.user.email], fail_silently=False)


class PostBlogUpdateView(UpdateView):
    model = PostBlog
    success_url = reverse_lazy('mainapp:blog_list')
    form_class = PostblogReadForm


class PostBlogDeleteView(DeleteView):
    model = PostBlog
    success_url = reverse_lazy('mainapp:blog_list')
