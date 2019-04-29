from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField("博客分类",max_length=100)
    index = models.IntegerField(default=999,verbose_name='分类排序')
        class Meta:
            verbose_name = '博客分类'
            verbose_name_plural = verbose_name
            def __str__(self):
                        return name
