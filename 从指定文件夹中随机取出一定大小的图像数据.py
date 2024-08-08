import os
import shutil
import random


def collect_images(source_folders, target_folder, total_images=3000):
    images_per_folder = total_images // len(source_folders)

    all_images = []
    for folder in source_folders:
        images = [os.path.join(folder, f) for f in os.listdir(folder)
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff'))]
        random.shuffle(images)
        all_images.append(images[:images_per_folder])

    selected_images = [img for sublist in all_images for img in sublist]

    remaining_images_needed = total_images - len(selected_images)
    if remaining_images_needed > 0:
        remaining_images = []
        for images in all_images:
            remaining_images.extend(images[images_per_folder:])
        random.shuffle(remaining_images)
        selected_images.extend(remaining_images[:remaining_images_needed])

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for image_path in selected_images:
        shutil.move(image_path, os.path.join(target_folder, os.path.basename(image_path)))


if __name__ == "__main__":
    source_folders = [
        input("请输入第一个源文件夹路径："),
        input("请输入第二个源文件夹路径："),
        input("请输入第三个源文件夹路径："),
        input("请输入第四个源文件夹路径：")
    ]
    target_folder = input("请输入目标文件夹路径：")

    collect_images(source_folders, target_folder)
