# python
# -*- coding:utf-8 -*-
# @FileName  :遍历xml文件并修改标签名.py
# @Time      :2024/7/10 17:35
# @Author    :JHX


import os
import xml.etree.ElementTree as ET


def add_rotation_to_labels(xml_folder, angle):
    # 获取文件夹中的所有xml文件
    xml_files = [f for f in os.listdir(xml_folder) if f.lower().endswith('.xml')]

    for xml_file in xml_files:
        xml_path = os.path.join(xml_folder, xml_file)

        # 解析XML文件
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # 遍历所有object标签
        for obj in root.findall('object'):
            name = obj.find('name')
            if name is not None:
                # 添加rotation_{角度}到标签名后面
                name.text = f"{name.text}_rotation_{angle}"

        # 将修改后的XML文件保存回去
        tree.write(xml_path)
        print(f"已更新标签文件: {xml_path}")


# 示例调用
xml_folder = r'F:\datasets1_labels_rotation\train_labels\rotation_0_labels'  # 替换为实际的xml文件夹路径   这句代码中 r 代表 原始字符串 (raw string)
angle = 0  # 替换为你希望添加的角度

add_rotation_to_labels(xml_folder, angle)
