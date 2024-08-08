import os
import cv2

# 尝试读取当前目录下的一个测试图像文件
test_file_path = 'F:\\0-label_dataset\\0-finished\\images-merge-ori\\1708925663_83785.jpg'  # 确保在当前目录下有一个名为 test_image.jpg 的图像文件

# 检查测试文件路径是否存在
if not os.path.exists(test_file_path):
    print(f"测试文件路径不存在: {test_file_path}")
else:
    # 尝试读取测试图像
    img = cv2.imread(test_file_path)
    img_height, img_width, _ = img.shape
    print(img_height)
    print(img_width)

    # 检查是否读取成功
    if img is None:
        print(f"无法读取测试图像文件: {test_file_path}")
    else:
        print("测试图像读取成功")
        # 显示图像大小
        print(f"图像尺寸: {img.shape}")

        # 显示图像
        cv2.imshow("Test Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
