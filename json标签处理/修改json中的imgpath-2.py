# python
# -*- coding:utf-8 -*-
# @FileName  :修改json中的imgpath.py
# @Time      :2024/8/22 14:04
# @Author    :JHX

import os
import json

def process_json(input_json_file, output_json_file):
    print("input_json_file",input_json_file)
    print("output_json_file",output_json_file)
    file_in = open(input_json_file, "r")
    file_out = open(output_json_file, "w")
    # load数据到变量json_data
    json_data = json.load(file_in)
    imagePath = json_data["imagePath"]
    #截取路径中图像的文件名
    new_imagePath = imagePath.split("\\")[-1]
    # 修改json中图像路径
    json_data["imagePath"] = new_imagePath
    print(json_data)
    # 将修改后的数据写回文件
    file_out.write(json.dumps(json_data))
    file_in.close()
    file_out.close()

filePath = './anns'
file_list = os.listdir(filePath)
print(file_list)
for file_json in file_list:
    file_json_read = filePath+"/"+file_json
    print(type(file_json_read))
    file_json_write = "./new_anns/"+file_json
    process_json(file_json_read,file_json_write)
