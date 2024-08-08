import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET
import random


# 仅在读取中文路径的图像时使用如下函数
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), -1)
    return cv_img

def rotate_point(point, M):
    """旋转单个点"""
    point_new = np.dot(M, np.array([point[0], point[1], 1]))
    return int(point_new[0]), int(point_new[1])

def update_xml(xml_path, M, img_shape, new_img_shape):
    """更新XML标签文件"""
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # 旋转四个顶点
        point1 = (xmin, ymin)
        point2 = (xmax, ymin)
        point3 = (xmax, ymax)
        point4 = (xmin, ymax)

        rotated_points = [rotate_point(point, M) for point in [point1, point2, point3, point4]]
        x_coords = [p[0] for p in rotated_points]
        y_coords = [p[1] for p in rotated_points]

        # 获取新的边界框
        xmin_new = max(0, min(x_coords))
        ymin_new = max(0, min(y_coords))
        xmax_new = min(new_img_shape[1], max(x_coords))
        ymax_new = min(new_img_shape[0], max(y_coords))

        # 更新XML文件中的bbox
        bbox.find('xmin').text = str(xmin_new)
        bbox.find('ymin').text = str(ymin_new)
        bbox.find('xmax').text = str(xmax_new)
        bbox.find('ymax').text = str(ymax_new)

    return tree

def rotate_image_and_label(img_path, xml_path, angle, img_save_path, xml_save_path):
    # 读取图像
    img = cv_imread(img_path)
    if img is None:
        print(f"无法读取图像文件: {img_path}")
        return

    img_height, img_width = img.shape[:2]

    # 旋转矩阵
    M = cv2.getRotationMatrix2D((img_width / 2, img_height / 2), angle, 1)

    # 计算旋转后的图像尺寸
    abs_cos = abs(M[0, 0])
    abs_sin = abs(M[0, 1])
    bound_w = int(img_height * abs_sin + img_width * abs_cos)
    bound_h = int(img_height * abs_cos + img_width * abs_sin)
    M[0, 2] += bound_w / 2 - img_width / 2
    M[1, 2] += bound_h / 2 - img_height / 2

    # 旋转图像
    rotated_img = cv2.warpAffine(img, M, (bound_w, bound_h))

    # 保存旋转后的图像
    img_save_name = os.path.join(img_save_path, os.path.basename(img_path))
    cv2.imwrite(img_save_name, rotated_img)

    # 更新并保存XML标签文件
    tree = update_xml(xml_path, M, img.shape, rotated_img.shape)
    xml_save_name = os.path.join(xml_save_path, os.path.basename(xml_path))
    tree.write(xml_save_name)

if __name__ == '__main__':
    img_dir = 'F:\\0-label_dataset\\1-ori-newversion\\1-表箱汇总\\1-标准计量箱\\images'
    xml_dir = 'F:\\0-label_dataset\\1-ori-newversion\\1-表箱汇总\\1-标准计量箱\\xmls'
    base_save_path = 'F:\\label_dataset_enhanced\\1-ori-newversion\\1-表箱汇总\\1-标准计量箱'

    angles = [0, 90, 180, 270]  # 可能的旋转角度

    for angle in angles:
        img_save_path = os.path.join(base_save_path, f'rotation_{angle}', 'images')
        xml_save_path = os.path.join(base_save_path, f'rotation_{angle}', 'labels')

        if not os.path.exists(img_save_path):
            os.makedirs(img_save_path)
        if not os.path.exists(xml_save_path):
            os.makedirs(xml_save_path)

    for img_file in os.listdir(img_dir):
        if img_file.endswith('.jpg') or img_file.endswith('.png'):
            img_path = os.path.join(img_dir, img_file)
            xml_path = os.path.join(xml_dir, os.path.splitext(img_file)[0] + '.xml')
            if os.path.exists(xml_path):
                angle = random.choice(angles)  # 随机选择一个角度
                img_save_path = os.path.join(base_save_path, f'rotation_{angle}', 'images')
                xml_save_path = os.path.join(base_save_path, f'rotation_{angle}', 'labels')
                rotate_image_and_label(img_path, xml_path, angle, img_save_path, xml_save_path)
            else:
                print(f"对应的XML文件不存在: {xml_path}")
