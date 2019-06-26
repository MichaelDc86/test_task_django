from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.


class Blogger(AbstractUser):
    name = models.CharField(verbose_name='blogger_name', max_length=128, default='your_name')
    email = models.EmailField('email address', blank=True, unique=True)
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.SmallIntegerField(verbose_name='возраст', default=18)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(verbose_name='blog_name', max_length=128, default='new_blog')
    blogger = models.OneToOneField(Blogger, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PostBlog(models.Model):
    blogger = models.OneToOneField(Blogger, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, verbose_name='blog name', on_delete=models.CASCADE)
    title = models.CharField(verbose_name='title', max_length=128)
    text = models.CharField(verbose_name='text', max_length=256)
    date = models.DateTimeField(verbose_name='created', auto_now_add=True)

    def __str__(self):
        return self.title
