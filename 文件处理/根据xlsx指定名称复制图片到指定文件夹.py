# python
# -*- coding:utf-8 -*-
# @FileName  :根据xlsx指定名称复制图片到指定文件夹.py
# @Time      :2024/7/18 16:02
# @Author    :JHX


import os
import shutil
import pandas as pd

# 读取xlsx文件
file_path = r'E:\python_project\ultralytics\高唐20-21w.xlsx'
df = pd.read_excel(file_path)

# 设置源文件夹和目标文件夹
source_folder = r'F:\8-聊城20240513\高唐20-21w'
destination_root = r'D:\datasets\offline_out_in_classify'

# 遍历df中的每一行
for index, row in df.iterrows():
    image_name = row['Image Name']
    predicted_class = row['Predicted Class']

    # 只处理 Predicted Class 为 'out' 的情况        这里的类别也可以修改成其他的
    if predicted_class == 'out':
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
