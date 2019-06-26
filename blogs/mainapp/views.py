from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import resolve_url
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

from mainapp.models import PostBlog

from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

# Create your views here.


class BlogListView(ListView, LoginRequiredMixin):
    # queryset = PostBlog.objects.all().order_by('date')
    # request = self.request
    def get(self, request, *args, **kwargs):
        # print(request)
        queryset = PostBlog.objects.filter(user=request.blogger).order_by('date')
        # paginate_by = 3
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'blog'

        return context


class BloggerLogin(LoginView):
    template_name = 'mainapp/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
        auth_login(self.request, form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return HttpResponseRedirect(redirect_to)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    @method_decorator(sensitive_post_parameters('password'))
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(BloggerLogin, self).dispatch(request, *args, **kwargs)


class BloggerLogout(View):
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(settings.LOGOUT_REDIRECT_URL)
