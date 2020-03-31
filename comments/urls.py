#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 26/2/20
''
__author__ = "Ben ZHONG"
__date__ = '26/2/20 10:57 AM'

"""

"""

# 
from django.urls import path

from . import views
#

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]




if __name__ == '__main__':
    
    
    
    
    pass























