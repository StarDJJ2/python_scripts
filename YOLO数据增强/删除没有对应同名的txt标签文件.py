# python
# -*- coding:utf-8 -*-
# @FileName  :删除没有对应同名的txt标签文件.py
# @Time      :2024/7/12 16:50
# @Author    :JHX


import os

def remove_unmatched_txt_labels(image_folder, txt_folder):
    # 获取图像文件夹中的所有图像文件名（不包括扩展名）
    image_files = {os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))}

    # 获取txt文件夹中的所有txt文件名（不包括扩展名）
    txt_files = {f for f in os.listdir(txt_folder) if f.lower().endswith('.txt')}

    # 找出没有对应图像文件的txt文件
    unmatched_txt_files = {f for f in txt_files if os.path.splitext(f)[0] not in image_files}

    # 删除没有对应图像文件的txt文件
    for txt_file in unmatched_txt_files:
        txt_path = os.path.join(txt_folder, txt_file)
        os.remove(txt_path)
        print(f"已删除无对应图像的TXT标签文件: {txt_path}")

# 示例调用
image_folder = r'D:\datasets\Det-cabinet-5v\val\images'  # 替换为实际的图像文件夹路径
txt_folder = r'D:\datasets\Det-cabinet-5v\val\labels'  # 替换为实际的txt文件夹路径
remove_unmatched_txt_labels(image_folder, txt_folder)
