# python
# -*- coding:utf-8 -*-
# @FileName  :归一化YOLO的txt标签文件.py
# @Time      :2024/7/12 17:47
# @Author    :JHX

import os

def read_files(directory):
    """Read all files in the specified directory."""
    files_data = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            with open(filepath, 'r') as file:
                files_data[filepath] = file.readlines()
    return files_data

def normalize_coordinates(data, image_width, image_height):
    """Normalize coordinates and ensure they are within bounds."""
    normalized_lines = []
    for line in data:
        numbers = [float(num) for num in line.split()]
        normalized_numbers = []
        for i, num in enumerate(numbers):
            if i % 2 == 0:  # x coordinate
                normalized_num = num / image_width
            else:  # y coordinate
                normalized_num = num / image_height

            # Ensure coordinates are within [0, 1]
            normalized_num = max(0.0, min(1.0, normalized_num))
            normalized_numbers.append(normalized_num)

        normalized_lines.append(" ".join(map(str, normalized_numbers)) + "\n")
    return normalized_lines

def write_files(files_data):
    """Write the normalized data back to the files."""
    for filepath, data in files_data.items():
        with open(filepath, 'w') as file:
            file.writelines(data)

def main(directory, image_width, image_height):
    files_data = read_files(directory)
    for filepath, data in files_data.items():
        files_data[filepath] = normalize_coordinates(data, image_width, image_height)
    write_files(files_data)

if __name__ == "__main__":
    directory = '/path/to/your/labels'  # Replace with the path to your directory
    image_width = 640  # Replace with your image width
    image_height = 480  # Replace with your image height
    main(directory, image_width, image_height)