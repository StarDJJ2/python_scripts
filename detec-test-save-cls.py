from ultralytics import YOLO
from PIL import Image
import cv2
import os
import fnmatch
import numpy as np
import torch
import shutil
 

def get_images_in_directory(directory):  
    image_files = []  
    for root, dirs, files in os.walk(directory):  
        for file in fnmatch.filter(files, '*.jpg'):  
            image_files.append(os.path.join(root, file))  
        for file in fnmatch.filter(files, '*.jpeg'):  
            image_files.append(os.path.join(root, file))  
        for file in fnmatch.filter(files, '*.png'):  
            image_files.append(os.path.join(root, file))  
        for file in fnmatch.filter(files, '*.tiff'):  
            image_files.append(os.path.join(root, file))  
        for file in fnmatch.filter(files, '*.jfif'):  
            image_files.append(os.path.join(root, file))  
    return image_files  

model_cabinetcls = YOLO("./runs/detect/CabinetClassifyDet-2v/weights/best.pt")
# model_winlock= YOLO("./runs/detect/det-blade-BQ3/weights/best.pt")


imgpath = r'E:\data-wind-turbine\data-static_inspect\20221109_广西50\allimages-crop-train'
savepath = r'E:\data-wind-turbine\data-static_inspect\0-缺陷识别训练集\2-补漆分类（标注数据筛选）\train\BQ\images'
if not os.path.exists(savepath):
    os.makedirs(savepath)
imglist = get_images_in_directory(imgpath)
for i,imgname in enumerate(imglist): 
    print(i)
    basename = os.path.basename(imgname)
    try: 
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        # device = torch.device("cpu")
        res_cabinetcls = model_cabinetcls.predict(imgname,device =device,conf = 0.5,save=False)
        doorres = res_cabinetcls[0].cpu()
        bboxs = np.array(doorres.boxes.data).tolist()
        clses = np.array(doorres.boxes.cls).tolist()
        confs = np.array(doorres.boxes.conf).tolist()
        for i, cls1 in enumerate(clses):
            doorbbox = bboxs[i]
            conf = confs[i]
            # x1 = int(doorbbox[0])
            # y1 = int(doorbbox[1])
            # x2 = int(doorbbox[2])
            # y2 = int(doorbbox[3])
            if int(cls1) in [0,1,2]:
                # subpath = os.path.join(savepath,str(cls1))
                if not os.path.exists(savepath):
                    os.makedirs(savepath)
                # savename = os.path.join(subpath,basename.replace(".jpg","_"+str(conf)+".jpg"))
                # img = cv2.imdecode(np.fromfile(imgname, dtype=np.uint8), cv2.IMREAD_COLOR)
                # subimg = img[y1:y2,x1:x2,:]
                savename = os.path.join(savepath,basename)
                os.rename(imgname, savename)
    except:
        print("error:------"+basename)

