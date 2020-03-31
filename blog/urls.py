#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 27/12/19
''
__author__ = "Ben ZHONG"
__date__ = '27/12/19 6:35 PM'

"""

"""


from django.urls import path # 从 django.urls 导入了 path 函数

from . import views # 从当前目录下导入了 views 模块


# 把网址和处理函数的关系写在了 urlpatterns 列表里
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]



if __name__ == '__main__':
    
    
    
    
    pass























