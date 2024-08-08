# python
# -*- coding:utf-8 -*-
# @FileName  :图像名称对应的xml标签筛选.py
# @Time      :2024/7/10 17:14
# @Author    :JHX

import os

def remove_unmatched_images(image_folder, xml_folder):
    # 获取xml文件夹中的所有xml文件名（不包括扩展名）
    xml_files = {os.path.splitext(f)[0] for f in os.listdir(xml_folder) if f.lower().endswith('.xml')}

    # 获取图像文件夹中的所有图像文件名（不包括扩展名）
    image_files = {f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))}

    # 找出没有对应xml文件的图像文件
    unmatched_image_files = {f for f in image_files if os.path.splitext(f)[0] not in xml_files}

    # 删除没有对应xml文件的图像文件
    for image_file in unmatched_image_files:
        image_path = os.path.join(image_folder, image_file)
        os.remove(image_path)
        print(f"已删除无对应XML标签的图像文件: {image_path}")

# 示例调用
image_folder = r'F:\datasets2\val\rotation_0'  # 替换为实际的图像文件夹路径
xml_folder = r'F:\datasets1_labels_rotation\val_labels\rotation_0_labels'  # 替换为实际的xml文件夹路径
remove_unmatched_images(image_folder, xml_folder)
