# python
# -*- coding:utf-8 -*-
# @FileName  :xml标签的width和height数值交换.py
# @Time      :2024/7/17 11:07
# @Author    :JHX


import os
import xml.etree.ElementTree as ET


def swap_width_height(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    size = root.find('size')
    if size is not None:
        width = size.find('width')
        height = size.find('height')

        if width is not None and height is not None:
            width.text, height.text = height.text, width.text
            tree.write(xml_file)
            print(f'Swapped width and height in {xml_file}')


def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xml'):
            xml_file = os.path.join(folder_path, filename)
            swap_width_height(xml_file)


if __name__ == "__main__":
    folder_path = r'F:\width-height\val\rotation_270_labels'  # 将此处替换为你的文件夹路径
    process_folder(folder_path)
