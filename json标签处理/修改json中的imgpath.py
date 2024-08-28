# python
# -*- coding:utf-8 -*-
# @FileName  :修改json中的imgpath.py
# @Time      :2024/8/22 14:04
# @Author    :JHX

'''
目的：
    json文件中imagePath值不对要改过来
    具体不对：
        路径不对
逻辑：
    读取json
    获取imagePath值
    整改imagePath值（字典）
    字典写入json
其他：
    遍历文件夹json文件
'''
import json
import os


def load_json(json_dir):
    with open(json_dir, 'r', encoding='utf8') as js:
        data = json.load(js)
        js.close()
    return data


def rewrite_imgpath(json_dir, data):
    imgpath = data['imagePath']  # .split('\\')[-1]
    imgname = imgpath.split('\\')[-1]
    rewrie_imgpath = 'F:\server13_yaw_datasets\obb-data' + imgname  # 正确的路径 (路径修改)
    data['imagePath'] = rewrie_imgpath
    with open(json_dir, "w") as f:
        json.dump(data, f)
        f.close()


if __name__ == '__main__':
    json_path = "F:\server13_yaw_datasets\obb-data\json_labels"

    for file in os.listdir(json_path):  # json文件所在文件夹
        json_dir = os.path.join(json_path, file)  # json文件所在文件夹

        data = load_json(json_dir)
        rewrite_imgpath(json_dir=json_dir, data=data)