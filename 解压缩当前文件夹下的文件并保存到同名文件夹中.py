import os
import zipfile


def unzip_files(source_directory, target_directory):
    # 检查目标目录是否存在，如果不存在则创建
    os.makedirs(target_directory, exist_ok=True)

    # 遍历源目录中的所有文件
    for item in os.listdir(source_directory):
        # 如果文件是以 .zip 结尾的
        if item.endswith('.zip'):
            # 构建完整的文件路径
            file_path = os.path.join(source_directory, item)

            # 获取文件名（不包含扩展名）
            file_name = os.path.splitext(item)[0]

            # 构建解压缩目标文件夹路径
            extract_path = os.path.join(target_directory, file_name)

            # 创建目标文件夹（如果不存在）
            os.makedirs(extract_path, exist_ok=True)

            # 解压缩文件到目标文件夹
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)

            print(f'解压缩完成: {item} -> {extract_path}')


if __name__ == "__main__":
    # 示例：指定源目录和目标目录
    source_directory = 'F:/8-聊城20240513/聊城高唐'  # 替换为你的源目录路径
    target_directory = 'F:/8-聊城20240513/聊城高唐'  # 替换为你的目标目录路径

    unzip_files(source_directory, target_directory)
