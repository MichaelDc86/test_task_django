from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView

from mainapp.models import PostBlog, Blogger
from mainapp.forms import AdminShopUserRegisterForm

# Create your views here.


SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'
REDIRECT_FIELD_NAME = 'next'


class BlogListView(ListView, LoginRequiredMixin):

    template_name = 'mainapp/postblog_list.html'

    def get_queryset(self):  # , request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # blogs = Blogger[]
            # self.queryset = PostBlog.objects.filter(blog_id=self.request.user).order_by('date')
            blogs = self.request.user.subscription
            self.queryset = PostBlog.objects.filter(blog_id=blogs)
            return self.queryset
        else:
            return None

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = self.request.user  #'blog'

        return context


class BloggerRegister(CreateView):
    model = Blogger
    # template_name = 'adminapp/user_update.html'
    success_url = reverse_lazy('mainapp:login')
    form_class = AdminShopUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'create'
        return context


class BloggerLogin(LoginView):
    template_name = 'mainapp/login.html'
    # form_class = AuthenticationForm

    # def form_valid(self, form):
    #     redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
    #     auth_login(self.request, form.get_user())
    #     if self.request.session.test_cookie_worked():
    #         self.request.session.delete_test_cookie()
    #     return HttpResponseRedirect(redirect_to)

    # def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data(form=form))

    # @method_decorator(sensitive_post_parameters('password'))
    # def dispatch(self, request, *args, **kwargs):
    #     request.session.set_test_cookie()
    #     return super(BloggerLogin, self).dispatch(request, *args, **kwargs)

#     def form_valid(self, form):
#         # auth_login(self.request, form.get_user())
#         my_login(self.request, form.get_user())
#         return HttpResponseRedirect(self.get_success_url())
#
#
# def my_login(request, user, backend=None):
#     session_auth_hash = ''
#     if user is None:
#         user = request.user
#     if hasattr(user, 'get_session_auth_hash'):
#         session_auth_hash = user.get_session_auth_hash()
#         # session_auth_hash = user.get_session_auth_hash()
#
#     if SESSION_KEY in request.session:
#         if _get_user_session_key(request) != user.pk or (
#                 session_auth_hash and
#                 not constant_time_compare(request.session.get(HASH_SESSION_KEY, ''), session_auth_hash)):
#             request.session.flush()
#     else:
#         request.session.cycle_key()
#
#     try:
#         backend = backend or user.backend
#     except AttributeError:
#         backends = _get_backends(return_tuples=True)
#         if len(backends) == 1:
#             _, backend = backends[0]
#         else:
#             raise ValueError(
#                 'You have multiple authentication backends configured and '
#                 'therefore must provide the `backend` argument or set the '
#                 '`backend` attribute on the user.'
#             )
#     else:
#         if not isinstance(backend, str):
#             raise TypeError('backend must be a dotted import path string (got %r).' % backend)
#
#     request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
#     request.session[BACKEND_SESSION_KEY] = backend
#     request.session[HASH_SESSION_KEY] = session_auth_hash
#     if hasattr(request, 'user'):
#         request.user = user
#     rotate_token(request)
#     user_logged_in.send(sender=user.__class__, request=request, user=user)
