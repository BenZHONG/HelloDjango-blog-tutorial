#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ben ZHONG on 18/2/20
''
__author__ = "Ben ZHONG"
__date__ = '18/2/20 7:40 PM'

"""

"""

# 
from django import forms

from .models import Comment
#


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']




if __name__ == '__main__':
    
    
    
    
    pass























