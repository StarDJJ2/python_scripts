import os.path
import secrets
import cv2
import numpy as np
import xml.etree.ElementTree as ET


def replace_new_point(point: tuple, M, scale_x, scale_y):
    point_new = tuple(np.dot(M, np.array([point[0], point[1], 1]))[:2])
    point_new = (point_new[0] * scale_x, point_new[1] * scale_y)
    point_new = tuple(map(int, point_new))
    return point_new


def expend_image_label(img_path, label_path, scale_x, scale_y, angle, img_save_path: str, label_save_path: str,
                       is_fill=True, is_resize_on_raw=False, is_random_scale_x=False, is_random_scale_y=False,
                       is_random_angle=False, random_angle_tuple=None):
    """
    :param img_path: 读取的图像路径
    :param label_path: 读取的图像输入路径
    :param scale_x: 水平方向拉伸系数
    :param scale_y: 竖直方向拉伸系数
    :param angle: 图像旋转角度
    :param img_save_path: 生成图像的保存路径
    :param label_save_path: 生成标签的保存路径
    :param is_fill: 旋转会丢失信息，是否填充图像保留信息
    :param is_resize_on_raw: True按照原图比例resize, 否则在填充后的图像上进行resize
    :param is_random_scale_x: 是否随机水平方向拉伸
    :param is_random_scale_y: 是否随机竖直方向拉伸
    :param is_random_angle: 是否随机旋转角度
    :param random_angle_tuple: 如果传入了元组,只能在这个元组中随机选择旋转角度
    :return: None
    """
    if is_random_scale_x:
        scale_x = np.random.uniform(0.5, 1.5)
    if is_random_scale_y:
        scale_y = np.random.uniform(0.5, 1.5)
    if is_random_angle:
        if random_angle_tuple is None:
            angle = np.random.uniform(-10, 10)
        else:
            rand = secrets.randbelow(len(random_angle_tuple))  # [0,4) 取0-4之间的整数
            angle = random_angle_tuple[rand]
    dot = 4  # 保留小数点后几位
    # 读取图像
    img = cv2.imread(img_path)
    img_height, img_width, _ = img.shape

    # 旋转和拉伸图像
    rows, cols = img.shape[:2]
    # 旋转矩阵
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)

    if is_fill:
        temp_list = [replace_new_point((0, 0), M, 1, 1),
                     replace_new_point((0, img_height), M, 1, 1),
                     replace_new_point((img_width, 0), M, 1, 1),
                     replace_new_point((img_width, img_height), M, 1, 1)]
        n_x, n_y = zip(*temp_list)
        n_x = [-i if i < 0 else i - img_width for i in n_x if i > img_width or i < 0]
        n_y = [-i if i < 0 else i - img_height for i in n_y if i > img_height or i < 0]
        n_x = n_x if len(n_x) > 0 else [0]
        n_y = n_y if len(n_y) > 0 else [0]
        img_ = np.zeros((img_height + 2 * max(n_y), img_width + 2 * max(n_x), 3), dtype=np.uint8)
        img_[max(n_y):max(n_y) + img_height, max(n_x):max(n_x) + img_width] = img

        img = img_
        # 旋转后也不会缺失图像信息
        rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    img_rotated = cv2.warpAffine(img, M, (cols, rows))

    img_t = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2GRAY)

    h1, w1 = 0, 0
    for i in range(img_t.shape[0]):
        if not img_t[i, :].sum():
            h1 += 1
        else:
            break
    for i in range(img_t.shape[1]):
        if not img_t[:, i].sum():
            w1 += 1
        else:
            break
    img_rotated = img_rotated[h1:img_rotated.shape[0] - h1, w1:img_rotated.shape[1] - w1]
    rows, cols = img_rotated.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
    if is_resize_on_raw:
        img_rotated = cv2.resize(img_rotated, (int(img.shape[1] * scale_x), int(img.shape[0] * scale_y)))
    else:
        img_rotated = cv2.resize(img_rotated,
                                 (int(img_rotated.shape[1] * scale_x), int(img_rotated.shape[0] * scale_y)))
    cv2.imwrite(os.path.join(img_save_path, os.path.basename(img_path)), img_rotated)

    # 处理XML标签
    tree = ET.parse(label_path)
    root = tree.getroot()

    for obj in root.findall('object'):
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # 计算标记点的新位置
        point1 = (xmin, ymin)
        point2 = (xmax, ymin)
        point3 = (xmax, ymax)
        point4 = (xmin, ymax)

        # 将四个点组合起来
        l = [point1, point4, point2, point3]

        nl = []  # 把转化后的点添加这里
        for point in l:
            # 计算标记点point的新位置
            point_new = tuple(np.dot(M, np.array([point[0], point[1], 1]))[:2])
            if not is_resize_on_raw:
                point_new = (point_new[0] * scale_x, point_new[1] * scale_y)
            point_new = tuple(map(int, point_new))
            nl.append(point_new)

        ZIP = list(zip(nl[0], nl[1], nl[2], nl[3]))

        xmin_new = min(ZIP[0])
        ymin_new = min(ZIP[1])
        xmax_new = max(ZIP[0])
        ymax_new = max(ZIP[1])

        # 更新XML文件中的bbox
        bbox.find('xmin').text = str(xmin_new)
        bbox.find('ymin').text = str(ymin_new)
        bbox.find('xmax').text = str(xmax_new)
        bbox.find('ymax').text = str(ymax_new)

    # 保存更新后的XML文件
    tree.write(os.path.join(label_save_path, os.path.basename(label_path)))


if __name__ == '__main__':
    label_save_path = r'F:\label_dataset_enhanced\0-finished\xmls-merge-v5'  # 标签保存路径
    image_save_path = r'F:\label_dataset_enhanced\0-finished\images-merge-ori'  # 图片保存路径
    angle_ = 90  # 数据增强采用的图片旋转角度

    path_ = r'F:\0-label_dataset\0-finished'
    path1 = os.listdir(path_ + '/images-merge-ori')  # images/图片 所在路径

    for p in path1:
        im_p = os.path.join(path_, 'images-merge-ori', p)
        la_p = os.path.join(path_, 'xmls-merge-v5', p.split('.')[0] + '.xml')

        expend_image_label(img_path=im_p,
                           label_path=la_p, scale_x=1,
                           scale_y=1, angle=angle_, img_save_path=image_save_path,
                           label_save_path=label_save_path,
                           random_angle_tuple=(0, 90, 180, 270))
