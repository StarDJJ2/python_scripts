###############################################################################
#             match label/data and save in the specified location             #
# @Last-modified    : 2020-12-30                                              #
# @Author : Nanqing Liu                                                       #
# @Reconstruct By: Ze Si                                                      #
###############################################################################

import os
import shutil
import xml.etree.ElementTree as ET
from pathlib import Path
from tqdm import tqdm

# 定义基础目录
base_dir = r'F:\datasets_detect\train'

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

def convert_annotation(xml_paths, classes, save_dir):
    """
    将XML标注文件转换为TXT格式，并保存在指定目录下
    """
    for xml_path in tqdm(xml_paths, desc="Converting"):
        # 打开XML文件
        in_file = open(xml_path, encoding="utf-8")
        # 获取文件名（不含扩展名）
        name = os.path.basename(xml_path).split(".")[0]
        # 构建输出文件的路径和文件名
        out_file_name = Path(save_dir) / f"{name}.txt"
        # 打开输出文件
        out_file = open(str(out_file_name), 'w')
        # 解析XML
        tree = ET.parse(in_file)
        root = tree.getroot()
        # 获取图像尺寸
        size = root.find('size')
        w = int(float(size.find('width').text))
        h = int(float(size.find('height').text))
        item_counter = 0
        # 遍历所有对象
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            # 如果类别不在指定的类别列表中，或者标记为difficult，则跳过
            if cls not in classes or int(difficult) == 1:
                continue
            item_counter += 1
            # 获取类别ID
            cls_id = classes.index(cls)
            # 获取边界框坐标
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text),
                 float(xmlbox.find('xmax').text),
                 float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            # 转换边界框坐标为相对值，并写入输出文件
            bb = convert((w, h), b)
            out_file.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")
        out_file.close()
        # 如果未写入任何有效的对象，则删除生成的空文件
        if item_counter == 0:
            os.remove(out_file_name)

def process_subdirectories(base_dir, classes):
    # 遍历基础目录下的所有子目录
    for root, dirs, files in os.walk(base_dir):
        if 'images' in dirs:
            images_dir = os.path.join(root, 'images')
            label_dir = os.path.join(root, 'labels')
            labels_dir = os.path.join(root, 'txt_labels_norm')
            
            # 如果label文件夹不存在，则创建
            if not os.path.exists(label_dir):
                os.makedirs(label_dir)
                print(f"Created directory: {label_dir}")
            
            # 移动images文件夹中的xml文件到label文件夹中
            if os.path.exists(images_dir) and os.path.exists(label_dir):
                move_xml_files(images_dir, label_dir)
            
            # 清空labels文件夹中的内容
            clear_labels_directory(labels_dir)
            
            # 转换label文件夹中的xml文件为txt文件并保存到labels文件夹
            xml_files = list(Path(label_dir).glob("*.xml"))
            if xml_files:
                convert_annotation(xml_files, classes, labels_dir)

def move_xml_files(src_dir, dst_dir):
    # 遍历源目录下的所有文件
    for filename in os.listdir(src_dir):
        if filename.endswith('.xml'):
            src = os.path.join(src_dir, filename)
            dst = os.path.join(dst_dir, filename)
            
            # 移动xml文件到目标目录
            shutil.move(src, dst)
            print(f"Moved {filename} to {dst_dir}")

def clear_labels_directory(labels_dir):
    # 清空labels文件夹中的所有内容
    if os.path.exists(labels_dir):
        for filename in os.listdir(labels_dir):
            file_path = os.path.join(labels_dir, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")
        print(f"Deleted all contents in {labels_dir}")

if __name__ == "__main__":
    # 定义类别列表
    classes = ['1.normal-cabinet_rotation_0', '1.normal-cabinet_rotation_90', '1.normal-cabinet_rotation_180', '1.normal-cabinet_rotation_270']

    # 执行处理函数
    process_subdirectories(base_dir, classes)
