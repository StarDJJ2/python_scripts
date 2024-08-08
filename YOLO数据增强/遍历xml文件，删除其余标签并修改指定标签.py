# python
# -*- coding:utf-8 -*-
# @FileName  :遍历xml文件，删除其余标签并修改指定标签.py
# @Time      :2024/7/12 13:54
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

        # 获取所有object标签
        objects = root.findall('object')
        # 过滤出name不为'1.normal-cabinet'的object标签并删除
        objects_to_keep = []
        for obj in objects:
            name = obj.find('name')
            if name is not None and name.text == '1.normal-cabinet':
                objects_to_keep.append(obj)
            else:
                root.remove(obj)

        # 如果objects_to_keep为空，说明没有'1.normal-cabinet'标签，删除该xml文件
        if not objects_to_keep:
            os.remove(xml_path)
            print(f"已删除标签文件: {xml_path}")
            continue

        # 对剩下的objects添加rotation_{角度}到标签名后面
        for obj in objects_to_keep:
            name = obj.find('name')
            name.text = f"{name.text}_rotation_{angle}"

        # 将修改后的XML文件保存回去
        tree.write(xml_path)
        print(f"已更新标签文件: {xml_path}")

# 示例调用
xml_folder = r'F:\datasets1_labels_rotation\val_labels\rotation_270_labels'  # 替换为实际的xml文件夹路径
angle = 270  # 替换为你希望添加的角度

add_rotation_to_labels(xml_folder, angle)
