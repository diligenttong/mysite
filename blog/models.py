# coding:utf8
from __future__ import unicode_literals
from django.urls import reverse
from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
import datetime
from django.template.defaultfilters import slugify
from unidecode import unidecode


# Create your models here.

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', '草稿'),
        ('p', '发表'),
    )
    title = models.CharField(u"博客标题", max_length=100)  # 博客标题
    slug = models.SlugField('slug', max_length=60)
    pub_date = models.DateTimeField(u"发布日期", auto_now_add=True, editable=True)  # 博客发布日期
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间', auto_now=True, null=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES, default='p')
    author = models.ForeignKey(to=User, verbose_name='作者', on_delete=models.CASCADE)
    views = models.PositiveIntegerField('浏览量', default=0)
    body = models.TextField()
    category = models.ForeignKey(to='Category', verbose_name='分类', on_delete=models.CASCADE)

    # tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)

    class Meta:
        ordering = ("-update_time",)
        index_together = (('id', 'slug'),)

    #     对数据库中的这两个字段建立索引

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id or not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)
        # 对save方法进行重写，目的是为了使slug等于title

    def get_absolute_url(self):
        # 获取某篇文章的URL
        return reverse("blog:article_detail", args=[self.id, self.slug])


class Category(models.Model):
    """文章分类"""
    name = models.CharField('分类名', max_length=30, unique=True)
    slug = models.SlugField('slug', max_length=40)
    user = models.ForeignKey(to=User, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# class Tag(models.Model):
#     """文章标签"""
#     name = models.CharField('标签名', max_length=30, unique=True)
#     slug = models.SlugField('slug', max_length=40)
#
#     def __str__(self):
#         return self.name
#
#     def get_absolute_url(self):
#         return reverse('blog:tag_detail', args=[self.slug])
#
#     def get_article_count(self):
#         return Article.objects.filter(tags__slug=self.slug).count()
#
#     class Meta:
#         ordering = ['name']
#         verbose_name = "标签"
#         verbose_name_plural = verbose_name
