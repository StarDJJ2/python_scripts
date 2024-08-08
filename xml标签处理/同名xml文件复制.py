# python
# -*- coding:utf-8 -*-
# @FileName  :同名xml文件复制.py
# @Time      :2024/8/7 11:49
# @Author    :JHX


import os
import shutil

def copy_matching_xml_files(image_folder, xml_folder, destination_folder):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取图像文件名（不包含扩展名）
    image_names = set(os.path.splitext(f)[0] for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')))

    # 遍历XML文件夹，复制与图像同名的XML文件
    for file in os.listdir(xml_folder):
        if file.lower().endswith('.xml'):
            file_name_without_ext = os.path.splitext(file)[0]
            if file_name_without_ext in image_names:
                source_file_path = os.path.join(xml_folder, file)
                destination_file_path = os.path.join(destination_folder, file)
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied {source_file_path} to {destination_file_path}")

# 定义文件夹路径
image_folder = r'D:\blade_datasets_processed\黑崖子风场_val\images\Normal_2000'  # images文件夹
xml_folder = r'D:\blade_datasets_processed\黑崖子风场_val\xml\Normal'   # xml文件夹
destination_folder = r'D:\blade_datasets_processed\黑崖子风场_val\xml\Normal_2000'

copy_matching_xml_files(image_folder, xml_folder, destination_folder)
