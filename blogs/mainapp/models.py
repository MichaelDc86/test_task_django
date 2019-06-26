from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

# Create your models here.


class Blogger(AbstractUser):
    email = models.EmailField('email address', blank=True, unique=True)
    avatar = models.ImageField(upload_to='users_avatar', blank=True)
    age = models.SmallIntegerField(verbose_name='возраст', default=18)
    # blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    # subscription = models.ManyToManyField()


class Blog(models.Model):
    blogger = models.OneToOneField(Blogger, on_delete=models.DO_NOTHING, related_name='+',)


class PostBlog(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='blog name', on_delete=models.DO_NOTHING, related_name='+',)
    title = models.CharField(verbose_name='title', max_length=128)
    text = models.CharField(verbose_name='text', max_length=256)
    date = models.DateTimeField(verbose_name='created', auto_now_add=True)
