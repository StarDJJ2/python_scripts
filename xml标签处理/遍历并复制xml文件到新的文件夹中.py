# python
# -*- coding:utf-8 -*-
# @FileName  :遍历并复制xml文件到新的文件夹中.py
# @Time      :2024/8/6 11:26
# @Author    :JHX


import os
import shutil

def copy_xml_files(source_folder1, source_folder2, destination_folder):
    # 遍历文件夹1中的子文件夹
    for subdir1 in os.listdir(source_folder1):
        subdir1_path = os.path.join(source_folder1, subdir1)
        if os.path.isdir(subdir1_path):
            # 获取文件夹1中子文件夹的图像文件名（不带扩展名）
            image_names = [os.path.splitext(file)[0] for file in os.listdir(subdir1_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

            # 对应的文件夹2中的子文件夹路径
            subdir2_path = os.path.join(source_folder2, subdir1)
            if os.path.isdir(subdir2_path):
                # 创建目标文件夹
                destination_subdir_path = os.path.join(destination_folder, subdir1)
                os.makedirs(destination_subdir_path, exist_ok=True)

                # 遍历文件夹2中的XML文件
                for file in os.listdir(subdir2_path):
                    if file.lower().endswith('.xml'):
                        file_name_without_ext = os.path.splitext(file)[0]
                        if file_name_without_ext in image_names:
                            # 复制XML文件到目标文件夹
                            source_file_path = os.path.join(subdir2_path, file)
                            destination_file_path = os.path.join(destination_subdir_path, file)
                            shutil.copy2(source_file_path, destination_file_path)
                            print(f"Copied {source_file_path} to {destination_file_path}")

if __name__ == "__main__":
    folder1 = r'D:\blade_datasets_processed\黑崖子风场_val\images\Normal_2000'  # images文件夹
    folder2 = r'D:\blade_datasets_processed\黑崖子风场_val\xml\Normal'   # xml文件夹
    destination_folder = r'D:\blade_datasets_processed\黑崖子风场_val\xml\Normal_2000'
    copy_xml_files(folder1, folder2, destination_folder)