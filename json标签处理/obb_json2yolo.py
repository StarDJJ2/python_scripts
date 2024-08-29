import json
import os


# 偏航角数据集json转yolo

path = r"E:\新添偏航角数据\8月菏泽动态风机\8.21\风机偏航数据"                    # 偏航角数据集json所在文件夹

target = r"E:\新添偏航角数据\偏航角模型更新20240829\labels\8.21"               # 转换后yolo标签所在文件夹


for name in os.listdir(path):
    if not name.endswith("json"):
        continue
    path_name = os.path.join(path, name)
    with open(path_name, 'r') as f:
        data = json.load(f)
        f.close()
    imageHeight = data["imageHeight"]
    imageWidth = data["imageWidth"]
    shapes = data["shapes"]

    points = None
    points_hub = None
    for shape in shapes:
        if shape['label'] == '5':
            points = shape["points"]
        if shape['label'] == '6':
            xy = shape["points"][0]
            points_hub = shape["points"]

    if points is not None:
        context_txt = "0 "
        for point in points:
            context_txt += str(point[0] / imageWidth) + " " + str(point[1] / imageHeight) + " "
        context_txt += "\n"

    if points_hub is not None:
        context_txt += "1 "
        for point in points_hub:
            context_txt += str(point[0] / imageWidth) + " " + str(point[1] / imageHeight) + " "
        context_txt += "\n"

    with open(os.path.join(target, name.replace("json", "txt")), 'w') as f:
        f.write(context_txt)
        f.close()
