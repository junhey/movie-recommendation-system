from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#电影类别
class Genres(models.Model):
    name = models.CharField(verbose_name="分类名称",max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


#电影
class Film(models.Model):
    name = models.CharField(verbose_name='电影名',max_length=20)
    brief = models.TextField(verbose_name='电影介绍')
    rate =models.CharField(verbose_name='电影评分',max_length=5)
    link = models.CharField(verbose_name='电影链接',max_length=50)
    img = models.CharField(verbose_name='电影图片',max_length=50)
    create_date = models.CharField(verbose_name='日期',max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '电影'
        verbose_name_plural = verbose_name


#评分
class Rating(models.Model):
    film = models.ForeignKey(Film,verbose_name='电影',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    rating = models.CharField(verbose_name='评分',max_length=20)
    time = models.CharField(verbose_name='时间',max_length=100)

    def __str__(self):
        return str(self.film)

    class Meta:
        verbose_name = '评分'
        verbose_name_plural = verbose_name

#系统参数
class Sysconfig(models.Model):
    k = models.CharField(verbose_name='k参数值',max_length=20)
    random = models.CharField(verbose_name='随机值',max_length=20)

    def __str__(self):
        return str(self.k)

    class Meta:
        verbose_name = '系统参数'
        verbose_name_plural = verbose_name

