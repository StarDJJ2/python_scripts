import os
from PIL import Image
import random


def rotate_images(input_folder, output_base_folder):
    # 确定输出文件夹名称
    output_folders = {0: 'rotation_0', 90: 'rotation_90', 180: 'rotation_180', 270: 'rotation_270'}

    # 创建输出文件夹
    for angle, folder in output_folders.items():
        path = os.path.join(output_base_folder, folder)
        if not os.path.exists(path):
            os.makedirs(path)

    # 获取所有图像文件
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # 确保图像文件数量是 4 的倍数
    num_files = len(image_files)
    if num_files % 4 != 0:
        raise ValueError("图像文件数量不是4的倍数，请调整图像文件数量。")

    # 随机打乱图像文件列表
    random.shuffle(image_files)

    # 确定每个文件夹应包含的图像数量
    files_per_folder = num_files // 4

    # 处理旋转和保存
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(input_folder, image_file)
        image = Image.open(image_path)

        # 确定当前图像应旋转的角度
        if i < files_per_folder:
            angle = 0
        elif i < 2 * files_per_folder:
            angle = 90
        elif i < 3 * files_per_folder:
            angle = 180
        else:
            angle = 270

        # 旋转图像
        rotated_image = image.rotate(angle, expand=True)

        # 保存图像到对应文件夹
        output_path = os.path.join(output_base_folder, output_folders[angle], image_file)
        rotated_image.save(output_path)

    print("图像旋转和保存完成！")


# 示例调用
input_folder = 'E:\\dataset\\meterbox_test_dataset'  # 替换为实际的输入文件夹路径
output_base_folder = 'E:\\dataset\\yolov8_classify_test'  # 替换为实际的输出文件夹路径
rotate_images(input_folder, output_base_folder)
