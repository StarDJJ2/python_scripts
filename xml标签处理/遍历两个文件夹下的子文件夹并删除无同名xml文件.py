# python
# -*- coding:utf-8 -*-
# @FileName  :遍历两个文件夹下的子文件夹并删除无同名xml文件.py
# @Time      :2024/8/6 13:50
# @Author    :JHX


import os
import shutil

def copy_and_clean_xml_files(source_folder1, source_folder2):
    # 遍历文件夹1中的子文件夹
    for subdir1 in os.listdir(source_folder1):
        subdir1_path = os.path.join(source_folder1, subdir1)
        if os.path.isdir(subdir1_path):
            # 获取文件夹1中子文件夹的图像文件名（不带扩展名）
            image_names = [os.path.splitext(file)[0] for file in os.listdir(subdir1_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

            # 对应的文件夹2中的子文件夹路径
            subdir2_path = os.path.join(source_folder2, subdir1)
            try:
                # 遍历文件夹2中的XML文件
                for file in os.listdir(subdir2_path):
                    if file.lower().endswith('.xml'):
                        file_name_without_ext = os.path.splitext(file)[0]
                        source_file_path = os.path.join(subdir2_path, file)
                        if file_name_without_ext in image_names:
                            continue
                        else:
                            # 删除没有对应图像的XML文件
                            os.remove(source_file_path)
                            print(f"Deleted {source_file_path}")
            except FileNotFoundError as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    folder1 = r'D:\blade_datasets_processed\黑崖子风场_val\images'  # images文件夹
    folder2 = r'D:\blade_datasets_processed\黑崖子风场_val\xml'   # xml文件夹
    copy_and_clean_xml_files(folder1, folder2)