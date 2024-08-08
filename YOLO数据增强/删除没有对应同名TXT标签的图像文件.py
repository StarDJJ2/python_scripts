# python
# -*- coding:utf-8 -*-
# @FileName  :删除没有对应同名TXT标签的图像文件.py
# @Time      :2024/7/12 16:45
# @Author    :JHX

import os

def remove_unmatched_images(image_folder, txt_folder):
    # 获取txt文件夹中的所有txt文件名（不包括扩展名）
    txt_files = {os.path.splitext(f)[0] for f in os.listdir(txt_folder) if f.lower().endswith('.txt')}

    # 获取图像文件夹中的所有图像文件名（不包括扩展名）
    image_files = {f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))}

    # 找出没有对应txt文件的图像文件
    unmatched_image_files = {f for f in image_files if os.path.splitext(f)[0] not in txt_files}

    # 删除没有对应txt文件的图像文件
    for image_file in unmatched_image_files:
        image_path = os.path.join(image_folder, image_file)
        os.remove(image_path)
        print(f"已删除无对应TXT标签的图像文件: {image_path}")

# 示例调用
image_folder = r'D:\datasets\Det-cabinet-5v\val\images'  # 替换为实际的图像文件夹路径
txt_folder = r'D:\datasets\Det-cabinet-5v\val\labels'  # 替换为实际的txt文件夹路径
remove_unmatched_images(image_folder, txt_folder)
