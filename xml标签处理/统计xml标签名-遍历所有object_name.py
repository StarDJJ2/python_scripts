# python
# -*- coding:utf-8 -*-
# @FileName  :统计xml标签名-遍历所有object_name.py
# @Time      :2024/7/22 15:03
# @Author    :JHX

import os
import xml.etree.ElementTree as ET


# 定义要统计的标签名
target_labels = ['1.normal-cabinet', '2.dooropen-cabinet', '3.dooroff-cabinet', '4.damage-cabinet', '5.severerust-cabinet', '6.foreignobject-cabinet', '26.slightrust-cabinet']

# 初始化计数器
label_counts = {label: 0 for label in target_labels}

# 指定要读取的文件夹路径
folder_path = r'D:\datasets\Det-cabinet-5v\xmls-train'  # 请将此路径替换为实际的文件夹路径

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xml'):  # 确保只处理XML文件
        file_path = os.path.join(folder_path, filename)
        try:
            # 解析XML文件
            tree = ET.parse(file_path)
            root = tree.getroot()

            # 查找第一个<object><name>标签
            for obj in root.findall('.//object'):
                name_tag = obj.find('name')
                if name_tag is not None and name_tag.text in target_labels:
                    label_counts[name_tag.text] += 1
        except ET.ParseError as e:
            print(f"Error parsing file {filename}: {e}")

# 打印各个标签的数量
for label, count in label_counts.items():
    print(f"Label '{label}': {count}")
