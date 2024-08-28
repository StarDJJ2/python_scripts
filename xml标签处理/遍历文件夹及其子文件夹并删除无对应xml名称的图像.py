# python
# -*- coding:utf-8 -*-
# @FileName  :遍历文件夹及其子文件夹并删除无对应xml名称的图像.py
# @Time      :2024/7/18 17:38
# @Author    :JHX

import os

def remove_unmatched_images(image_folder, xml_folder):
    # 获取xml文件夹中的所有xml文件名（不包括扩展名）
    xml_files = {os.path.splitext(f)[0] for f in os.listdir(xml_folder) if f.lower().endswith('.xml')}

    # 获取图像文件夹及其子文件夹中的所有图像文件名（包括扩展名）
    image_files = set()
    for root, _, files in os.walk(image_folder):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_files.add(os.path.join(root, f))

    # 找出没有对应xml文件的图像文件
    unmatched_image_files = {f for f in image_files if os.path.splitext(os.path.basename(f))[0] not in xml_files}

    # 删除没有对应xml文件的图像文件
    for image_file in unmatched_image_files:
        os.remove(image_file)
        print(f"已删除无对应XML标签的图像文件: {image_file}")

# 示例调用
image_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\images'  # 替换为实际的图像文件夹路径
xml_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\xmls_shaixuan'  # 替换为实际的xml文件夹路径
remove_unmatched_images(image_folder, xml_folder)
