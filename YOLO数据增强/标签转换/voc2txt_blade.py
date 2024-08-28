# python
# -*- coding:utf-8 -*-
# @FileName  :voc2txt_meterbox.py
# @Time      :2024/7/23 10:21
# @Author    :JHX

import os
import xml.etree.ElementTree as ET

def convert(size, box):
    """
    将边界框坐标从绝对像素值转换为相对于图像尺寸的比例
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)

def convert_annotation(xml_files_path, save_txt_files_path, classes):
    xml_files = os.listdir(xml_files_path)
    for xml_name in xml_files:
        xml_file = os.path.join(xml_files_path, xml_name)
        out_txt_path = os.path.join(save_txt_files_path, xml_name.split('.')[0] + '.txt')
        out_txt_f = open(out_txt_path, 'w')
        tree = ET.parse(xml_file)
        root = tree.getroot()
        size_element = root.find('size')
        w = int(size_element.find('width').text)
        h = int(size_element.find('height').text)

        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_txt_f.write(f"{cls_id} " + " ".join(f"{a:.6f}" for a in bb) + '\n')

        out_txt_f.close()

if __name__ == "__main__":
    # 需要转换的类别
    classes = ['BX', 'DQ', 'FS', 'Normal', 'TL', 'WR', 'BQ']
    # VOC格式的XML标签文件路径
    xml_files1 = r'D:\blade_datasets_processed_extracted1_chongbiaozhu\黑崖子风场_val\xml'
    # 转换为YOLO格式的TXT标签文件存储路径
    save_txt_files1 = r'D:\blade_datasets_processed_extracted1_chongbiaozhu\黑崖子风场_val\labels'

    convert_annotation(xml_files1, save_txt_files1, classes)
