# coding=utf-8

import xadmin
from xadmin import views
from .models import *

class BaseSetting(object):
    '''主题'''
    enable_themes=True
    use_bootswatch=True

class GlobalSetting(object):
    #页头title
    site_title='SS后台管理系统'
    #页脚公司
    site_footer='SS公司'
    #左侧菜单栏收起
    menu_style='accordion'


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
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
