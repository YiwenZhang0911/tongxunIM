from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


# Create your models here.

class User(AbstractBaseUser):
    accid = models.CharField(verbose_name='通信ID', max_length=25)
    name = models.CharField(verbose_name='通信昵称', max_length=25)
    token = models.CharField(verbose_name='token', max_length=36)

    class Meta(object):
        db_table = 'user'
        verbose_name = verbose_name_plural = '用户'
