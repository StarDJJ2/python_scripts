# python
# -*- coding:utf-8 -*-
# @FileName  :同名图像文件复制.py
# @Time      :2024/8/21 15:33
# @Author    :JHX

import os
import shutil

def copy_matching_image_files(image_folder, xml_folder, destination_folder):
    # 确保目标文件夹存在
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 获取XML文件名（不包含扩展名）
    xml_names = set(os.path.splitext(f)[0] for f in os.listdir(xml_folder) if f.lower().endswith('.xml'))

    # 遍历图像文件夹，复制与XML文件同名的图像文件
    for file in os.listdir(image_folder):
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            file_name_without_ext = os.path.splitext(file)[0]
            if file_name_without_ext in xml_names:
                source_file_path = os.path.join(image_folder, file)
                destination_file_path = os.path.join(destination_folder, file)
                shutil.copy2(source_file_path, destination_file_path)
                print(f"Copied {source_file_path} to {destination_file_path}")

# 定义文件夹路径
image_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\images'  # images文件夹
xml_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\xmls_shaixuan\2.dooropen-cabinet'   # xml文件夹
destination_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\images_shaixuan\2.dooropen-cabinet'

copy_matching_image_files(image_folder, xml_folder, destination_folder)
