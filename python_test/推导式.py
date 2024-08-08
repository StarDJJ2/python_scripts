# python
# -*- coding:utf-8 -*-
# @FileName  :推导式.py
# @Time      :2024/7/9 14:22
# @Author    :JHX

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper() if len(name)>3 else name.title() for name in names]
print(new_names)
