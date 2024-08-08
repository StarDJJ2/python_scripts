# python
# -*- coding:utf-8 -*-
# @FileName  :with as.py
# @Time      :2024/7/9 15:47
# @Author    :JHX


# with open('./test_runoob.txt') as f:
#     read_data = f.read()
#
# print(f.closed)


try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)
