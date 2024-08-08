# python
# -*- coding:utf-8 -*-
# @FileName  :根据xlsx对应名称复制图片到指定文件夹.py
# @Time      :2024/7/18 14:53
# @Author    :JHX


import os
import shutil
import pandas as pd

# 读取xlsx文件
file_path = r'E:\python_project\ultralytics\聊城茌平.xlsx'
df = pd.read_excel(file_path)

# 设置源文件夹和目标文件夹
source_folder = r'F:\8-聊城20240513\聊城茌平'
destination_root = r'D:\datasets\out_in_classify'

# 遍历df中的每一行
for index, row in df.iterrows():
    image_name = row['Image Name']
    predicted_class = row['Predicted Class']

    # 生成目标文件夹路径
    destination_folder = os.path.join(destination_root, predicted_class)

    # 如果目标文件夹不存在，创建它
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # 在源文件夹和子文件夹中搜索图像
    for root, dirs, files in os.walk(source_folder):
        if image_name in files:
            source_file_path = os.path.join(root, image_name)
            destination_file_path = os.path.join(destination_folder, image_name)

            # 复制文件到目标文件夹
            shutil.copy2(source_file_path, destination_file_path)
            print(f'Copied {image_name} to {destination_folder}')
            break
