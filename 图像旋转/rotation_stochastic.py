import os
import random
import fnmatch
from PIL import Image


def rotate_image(image_path, save_path):
    # 打开图像
    img = Image.open(image_path)
    # 随机选择旋转角度
    angle = random.choice([90, -90, 180])
    # 旋转图像
    rotated_img = img.rotate(angle)
    # 保存图像
    rotated_img.save(save_path)


def get_images_in_directory(directory):
    image_files = []
    patterns = ['*.jpg', '*.jpeg', '*.png', '*.tiff', '*.jfif']
    for root, dirs, files in os.walk(directory):
        for pattern in patterns:
            for file in fnmatch.filter(files, pattern):
                image_files.append(os.path.join(root, file))
    return image_files


def rotate_images_in_directory(input_directory, output_directory):
    # 创建输出目录
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 获取输入目录中的所有图像
    image_files = get_images_in_directory(input_directory)

    # 逐个旋转图像并保存到输出目录
    for image_path in image_files:
        # 获取图像文件名
        image_name = os.path.basename(image_path)
        # 构造保存路径
        save_path = os.path.join(output_directory, image_name)
        # 旋转图像并保存
        rotate_image(image_path, save_path)


# 输入目录
input_directory = r'E:\dataset\meterbox_test_dataset'
# 输出目录
output_directory = input_directory + '_rotation'

# 旋转并保存图像
rotate_images_in_directory(input_directory, output_directory)

print(f'所有图像已成功保存到 {output_directory}')
