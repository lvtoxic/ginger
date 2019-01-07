# coding=utf-8

import xadmin

from .models import *


class EmailVerifyRecordAdmin(object):
    # 列表名字
    list_display = ['code', 'email', 'send_type', 'send_time']
    # 搜索
    search_fields = ['code', 'email', 'send_type']
    # 过滤器
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    # 列表名字
    list_display = ['tiile', 'image', 'url', 'index', 'add_time']
    # 搜索
    search_fields = ['tiile', 'image', 'url', 'index']
    # 过滤器
    list_filter = ['tiile', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

