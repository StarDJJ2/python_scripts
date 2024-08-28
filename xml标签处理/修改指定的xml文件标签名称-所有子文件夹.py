# python
# -*- coding:utf-8 -*-
# @FileName  :修改指定的xml文件标签名称.py
# @Time      :2024/8/14 14:31
# @Author    :JHX
import os
import xml.etree.ElementTree as ET

def update_xml_files(folder_path):
    # 遍历文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".xml"):
                file_path = os.path.join(root, filename)

                # 解析XML文件
                tree = ET.parse(file_path)
                root_elem = tree.getroot()

                # 遍历XML中的所有<object><name>节点
                for obj in root_elem.findall('object'):
                    name = obj.find('name')
                    if name is not None and name.text == '2.normal-cabinet':
                        name.text = '1.normal-cabinet'
                        print(f"Updated {file_path}")

                # 保存修改后的XML文件
                tree.write(file_path, encoding='utf-8', xml_declaration=True)

# 指定要遍历的文件夹路径
folder_path = r'D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan'

# 更新XML文件
update_xml_files(folder_path)