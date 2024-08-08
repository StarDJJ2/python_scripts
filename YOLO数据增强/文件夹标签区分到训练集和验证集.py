# python
# -*- coding:utf-8 -*-
# @FileName  :文件夹标签区分到训练集和验证集.py
# @Time      :2024/7/10 17:19
# @Author    :JHX

import os
import shutil

def extract_and_save_xml(image_folder1, image_folder2, xml_folder, output_folder1, output_folder2):
    # 创建输出文件夹
    if not os.path.exists(output_folder1):
        os.makedirs(output_folder1)
    if not os.path.exists(output_folder2):
        os.makedirs(output_folder2)

    # 获取图像文件夹1中的所有图像文件名（不包括扩展名）
    image_files1 = {os.path.splitext(f)[0] for f in os.listdir(image_folder1) if
                    f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))}

    # 获取图像文件夹2中的所有图像文件名（不包括扩展名）
    image_files2 = {os.path.splitext(f)[0] for f in os.listdir(image_folder2) if
                    f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))}

    # 处理图像文件夹1中的图像对应的XML文件
    for image_file in image_files1:
        xml_file = os.path.join(xml_folder, f"{image_file}.xml")
        if os.path.exists(xml_file):
            shutil.copy(xml_file, os.path.join(output_folder1, f"{image_file}.xml"))
            print(f"已复制 {xml_file} 到 {output_folder1}")

    # 处理图像文件夹2中的图像对应的XML文件
    for image_file in image_files2:
        xml_file = os.path.join(xml_folder, f"{image_file}.xml")
        if os.path.exists(xml_file):
            shutil.copy(xml_file, os.path.join(output_folder2, f"{image_file}.xml"))
            print(f"已复制 {xml_file} 到 {output_folder2}")


# 示例调用
image_folder1 = r'F:\datasets1\train\rotation_90'  # 替换为实际的第一个图像文件夹路径
image_folder2 = r'F:\datasets1\val\rotation_90'  # 替换为实际的第二个图像文件夹路径
xml_folder = r'F:\label_dataset_enhanced_mixed\rotation_90\labels'  # 替换为实际的XML文件夹路径
output_folder1 = r'F:\datasets1_labels\train_labels\rotation_90_labels'  # 替换为实际的第一个输出文件夹路径
output_folder2 = r'F:\datasets1_labels\val_labels\rotation_90_labels'  # 替换为实际的第二个输出文件夹路径

extract_and_save_xml(image_folder1, image_folder2, xml_folder, output_folder1, output_folder2)
