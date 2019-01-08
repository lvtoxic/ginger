# coding=utf-8

import xadmin
from .models import *


class CourseAdmin(object):
    # 列表名字
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']
    # 搜索
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums']
    # 过滤器
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums', 'add_time']


class LessonAdmin(object):
    # 列表名字
    list_display = ['course', 'name', 'add_time']
    # 搜索
    search_fields = ['course', 'name']
    # 过滤器
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    # 列表名字
    list_display = ['lesson', 'name', 'add_time']
    # 搜索
    search_fields = ['lesson', 'name']
    # 过滤器
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    # 列表名字
    list_display = ['course', 'name', 'download', 'add_time']
    # 搜索
    search_fields = ['course', 'name', 'download']
    # 过滤器
    list_filter = ['course__name', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
