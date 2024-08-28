# python
# -*- coding:utf-8 -*-
# @FileName  :遍历多个文件夹进行文件替换.py
# @Time      :2024/8/27 上午10:43
# @Author    :JHX

import os
import shutil

# 定义文件夹路径列表，假设文件夹路径是绝对路径
folders = [
    # r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\1.normal-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\3.dooroff-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\2.dooropen-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\1.normal-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\4.damage-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\5.severerust-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\6.foreignobject-cabinet",
    r"D:\meterbox_defect_datasets\meterbox_yishaixuan_20240814\val_datasets\xmls_shaixuan\26.slightrust-cabinet"
]

# 获取第一个文件夹中的所有文件名
folder1_files = set(os.listdir(folders[0]))

# 遍历其他文件夹
for folder in folders[1:]:
    # 遍历当前文件夹中的所有文件
    for file_name in os.listdir(folder):
        # 检查文件是否在第一个文件夹中
        if file_name in folder1_files:
            # 如果存在，使用第一个文件夹中的文件替换当前文件夹中的文件
            src_file = os.path.join(folders[0], file_name)
            dest_file = os.path.join(folder, file_name)
            shutil.copy2(src_file, dest_file)
            print(f"Replaced {dest_file} with {src_file}")

print("文件替换完成！")
