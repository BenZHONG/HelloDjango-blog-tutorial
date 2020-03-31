#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 7/2/20
''
__author__ = "Ben ZHONG"
__date__ = '7/2/20 7:45 PM'

"""

"""

# 
from django import template

from ..models import Post, Category, Tag
#


register = template.Library()


@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num],
    }


@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC'),
    }


@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all(),
    }

if __name__ == '__main__':
    
    
    
    
    pass























