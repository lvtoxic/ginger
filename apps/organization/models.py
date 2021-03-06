# coding=utf-8
from datetime import datetime

from django.db import models


# Create your models here.


class CityDict(models.Model):
    '''
    城市
    '''
    name = models.CharField(max_length=20, verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now)
    desc = models.TextField(verbose_name='描述')

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(models.Model):
    '''
    课程机构
    '''
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    category = models.CharField(max_length=20, choices=(('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')),default='pxjg', verbose_name='机构类别')
    click_nums = models.IntegerField(default=0, verbose_name='点击人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='org/%Y/%M', verbose_name='logo', max_length=100)
    address = models.CharField(max_length=150, verbose_name='机构地址')
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name='所在城市')
    students=models.IntegerField(default=0, verbose_name='学习人数')
    course_nums=models.IntegerField(default=0, verbose_name='课程数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    '''
    教师
    '''
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name='所属机构')
    name = models.CharField(max_length=50, verbose_name='教师名字')
    work_years = models.IntegerField(default=0, verbose_name='工作年限')
    work_company = models.CharField(max_length=50, verbose_name='就职公司')
    work_position = models.CharField(max_length=50, verbose_name='公司职位')
    points = models.CharField(max_length=50, verbose_name='教学特点')
    click_nums = models.IntegerField(default=0, verbose_name='点击人数')
    fav_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
