from django.contrib import admin
from mainapp.models import Blogger, Blog, PostBlog


admin.site.register(Blogger)
admin.site.register(Blog)
admin.site.register(PostBlog)

# Register your models here.
