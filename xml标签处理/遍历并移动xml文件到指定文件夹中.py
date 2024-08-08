# python
# -*- coding:utf-8 -*-
# @FileName  :遍历并移动xml文件到指定文件夹中.py
# @Time      :2024/8/7 11:22
# @Author    :JHX


import os
import shutil


def move_xml_if_matched(image_folder, xml_folder, target_folder, image_extension=".jpg"):
    # 创建目标移动文件夹，如果不存在
    os.makedirs(target_folder, exist_ok=True)

    # 遍历图像文件夹，匹配图像和XML文件名
    for img_name in os.listdir(image_folder):
        # 提取图像文件名，移除后缀
        img_name, _ = os.path.splitext(img_name)
        img_path = os.path.join(image_folder, img_name) + image_extension

        # 检查对应的XML文件是否存在，格式为 img_name.xml
        xml_path = os.path.join(xml_folder, img_name + ".xml")

        if os.path.exists(xml_path):
            # 如果存在，移动XML文件到目标文件夹
            dest_path = os.path.join(target_folder, img_name + ".xml")
            shutil.move(xml_path, dest_path)
            print(f"Moved XML file {xml_path} to {dest_path}")
        else:
            print(f"No matching XML file for {img_name}")


# 调用函数，提供实际的文件夹路径
image_folder = r"D:\blade_datasets_processed\partion_blade_datasets_train\images\Normal_2000"
xml_folder = r"D:\blade_datasets_processed\partion_blade_datasets_train\xml\Normal"
target_folder = r"D:\blade_datasets_processed\partion_blade_datasets_train\xml\Normal_2000"  # 这里是移动XML的目标文件夹，如果有问题可以保持原路径，因为会被移动过去
move_xml_if_matched(image_folder, xml_folder, target_folder)
