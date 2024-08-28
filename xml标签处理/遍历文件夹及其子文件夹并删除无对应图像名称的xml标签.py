# python
# -*- coding:utf-8 -*-
# @FileName  :图像名称对应的xml标签筛选.py
# @Time      :2024/7/10 17:14
# @Author    :JHX

import os

def remove_unmatched_xml(image_folder, xml_folder):
    # 获取图像文件夹及其子文件夹中的所有图像文件名（不包括扩展名）
    image_files = set()
    for root, _, files in os.walk(image_folder):
        for f in files:
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_files.add(os.path.splitext(f)[0])

    # 获取xml文件夹中的所有xml文件名（不包括扩展名）
    xml_files = {os.path.splitext(f)[0] for f in os.listdir(xml_folder) if f.lower().endswith('.xml')}

    # 找出没有对应图像的xml文件
    unmatched_xml_files = xml_files - image_files

    # 删除没有对应图像的xml文件
    for xml_file in unmatched_xml_files:
        xml_path = os.path.join(xml_folder, f"{xml_file}.xml")
        os.remove(xml_path)
        print(f"已删除无对应图像的XML文件: {xml_path}")

# 示例调用
image_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\images'  # 替换为实际的图像文件夹路径
xml_folder = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\train_datasets\xmls'  # 替换为实际的xml文件夹路径
remove_unmatched_xml(image_folder, xml_folder)

