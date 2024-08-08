import os
import shutil
from PIL import Image

import os
from PIL import Image


def delete_small_images(directory):
    # 遍历目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查是否为图像文件
            if file.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(root, file)
                try:
                    # 首先检查图像大小
                    with Image.open(image_path) as img:           # 这里的Image.open执行完关闭后才能执行删除操作，这里也即是with块外才能执行删除图像的操作，不然会显示文件正在被占用
                        width, height = img.size

                    # 如果图像的宽度或高度小于640，则删除该文件
                    if min(width, height) < 640:
                        os.remove(image_path)
                        print(f"Deleted {image_path} because its size is less than 640x640.")
                except Exception as e:
                    print(f"Error processing {image_path}: {e}")

# 使用时，请确保已经安装了PIL库以及适用的Python环境

if __name__=='__main__':
    # size_threshold = 640            # 图像像素值大小
    delete_small_images(r"D:\blade_datasets_processed\partion_blade_datasets\images")
