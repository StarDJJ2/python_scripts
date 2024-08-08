import os
import shutil


def move_images_to_target_folder(source_folder, target_folder):
    # 遍历源文件夹中的所有子文件夹
    for root, dirs, files in os.walk(source_folder):
        # 跳过源文件夹本身
        if root == source_folder:
            continue

        for file in files:
            # 检查文件是否是图像文件（根据扩展名）
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                # 构建源文件路径和目标文件路径
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(target_folder, file)

                # 将图像文件移动到目标文件夹，如果有重复则覆盖
                shutil.move(src_file_path, dest_file_path)

        # 删除当前子文件夹
        shutil.rmtree(root)


if __name__ == "__main__":
    source_folder = input("请输入源文件夹路径：")
    target_folder = input("请输入目标文件夹路径：")

    # 检查目标文件夹是否存在，不存在则创建
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    move_images_to_target_folder(source_folder, target_folder)
