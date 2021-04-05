import glob
import os.path
from os import path
import cv2
from tqdm import tqdm
def unconvert(size, class_id, x, y, w, h):
    width, height = size
    xmax = int((x*width) + (w * width)/2.0)
    xmin = int((x*width) - (w * width)/2.0)
    ymax = int((y*height) + (h * height)/2.0)
    ymin = int((y*height) - (h * height)/2.0)
    class_id = int(class_id)
    h = ymax - ymin
    w = xmax - xmin
    return (class_id, xmin, ymin, w, h)
    
if path.exists("res") == False:
    os.mkdir("res")
for annot_path in tqdm(glob.glob("*.txt")):
    # print(annot_path)
    img_path = annot_path.split(".")[0]
    if path.exists(img_path+".jpg") == False:
        img_path = img_path+".png"
    else:
        img_path = img_path+".jpg"
    img = cv2.imread(img_path)
    height, width, _ = img.shape
    size = (float (width),float( height))

    file = open(annot_path)
    l = sum (1 for _ in file)
    file = open(annot_path)
    for i in range(l):
        class_id, x, y, w, h = file.readline().split(" ")
        x = float(x)
        y = float(y)
        w = float(w)
        h = float(h)
        contents = unconvert(size, class_id, x, y, w, h)
        new_file = open("res/"+annot_path, mode = 'a')
        new_file.write(str(contents[0])+" "+str(contents[1])+" "+str(contents[2])+" "+str(contents[4])+"\n")