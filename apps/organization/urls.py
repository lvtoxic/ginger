# coding=utf-8

from django.urls import path, re_path, include
from .views import OrgView, AddUserAskView

# app_name='org'
urlpatterns = [
    # 课程机构列表页
    path('list/', OrgView.as_view(), name='org_list'),
    path('add_ask/', AddUserAskView.as_view(), name='add_ask'),

]
