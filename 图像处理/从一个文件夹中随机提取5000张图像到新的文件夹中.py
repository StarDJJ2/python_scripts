# python
# -*- coding:utf-8 -*-
# @FileName  :从一个文件夹中随机提取5000张图像到新的文件夹中.py
# @Time      :2024/8/6 14:40
# @Author    :JHX


import os
import random
import shutil
import datetime

# 设置固定的随机数种子
random.seed(42)  # 使用一个示例种子值，你可以根据需要替换为任何整数

# 定义源文件夹和目标文件夹
source_folder = r"D:\blade_datasets_processed\黑崖子风场_val\images\Normal"
target_folder = r"D:\blade_datasets_processed\黑崖子风场_val\images\Normal_2000"  # 新的文件夹名
target_folder_path = os.path.join(os.getcwd(), target_folder)  # 创建到当前工作目录的文件夹路径

# 创建目标文件夹
os.makedirs(target_folder_path, exist_ok=True)

# 获取源文件夹中的所有图像文件（这里用".jpg"作为图片扩展名，你可以根据实际情况修改）
image_files = [os.path.join(source_folder, file) for file in os.listdir(source_folder) if file.endswith(".jpg")]

# 随机选择并复制5000张图像
selected_images = random.sample(image_files, 2000)  # 使用random.sample确保不重复选取

# 复制选择的图像到目标文件夹
for image_file in selected_images:
    copy_to = os.path.join(target_folder_path, os.path.basename(image_file))
    shutil.copy(image_file, copy_to)

# 打印任务完成的消息
print(f"已随机复制2000张图像到'{target_folder_path}'。要重现这个操作，请确保使用相同的随机种子(42)。")
