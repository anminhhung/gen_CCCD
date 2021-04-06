import os
import cv2
import glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import random 
from tqdm import tqdm


# Convert bbox background
def get_location(size, class_id, x, y, w, h):
    width, height = size
    xmax = int((x*width) + (w * width)/2.0)
    xmin = int((x*width) - (w * width)/2.0)
    ymax = int((y*height) + (h * height)/2.0)
    ymin = int((y*height) - (h * height)/2.0)
    class_id = int(class_id)
    h = ymax - ymin
    w = xmax - xmin

    return (class_id, xmin, ymin, h)

def convert(image_path, annot_path):   
    term=[]

    img = cv2.imread(image_path)
    
    height, width, _ = img.shape
    size = (float (width),float( height))
    open(annot_path, mode = 'a')
    file = open(annot_path)
    lines = file.readlines()
    
    for line in lines:
        class_id, x, y, w, h = line.replace("\n","").split(" ")
        x = float(x)
        y = float(y)
        w = float(w)
        h = float(h)
        contents = get_location(size, class_id, x, y, w, h)
        term.append(contents)
    return term

if os.path.exists("gendata") == False:
    os.mkdir("gendata")

'''
    format name: opencv_<image_name>_<count>.jpg
'''
def addTextWithOpenCV(image_path, annot_path, image_name, number_gen=10, dest_dir="gendata"):
    # Get dict
    GiaTriDen_info_list = open("dictionary/GiaTriDen.txt",encoding = 'utf-8').readlines()
    GioiTinh_info_list = open("dictionary/GioiTinh.txt",encoding = 'utf-8').readlines()
    HoTen_info_list = open("dictionary/HoTen.txt",encoding = 'utf-8').readlines()
    NgayThangSinh_info_list = open("dictionary/NgayThangSinh.txt",encoding = 'utf-8').readlines()
    NoiThuongTruTren_info_list = open("dictionary/NoiThuongTruTren.txt",encoding = 'utf-8').readlines()
    NoiThuongTruDuoi_info_list = open("dictionary/NoiThuongTruDuoi.txt",encoding = 'utf-8').readlines()
    QueQuan_info_list = open("dictionary/QueQuan.txt",encoding = 'utf-8').readlines()
    QuocTich_info_list = open("dictionary/QuocTich.txt",encoding = 'utf-8').readlines()
    So_info_list = open("dictionary/So.txt",encoding = 'utf-8').readlines()

    count=0
    for _ in tqdm(range(number_gen)):
        #get background in list
        info = convert(image_path, annot_path)
        
        So, HoTen,NgayThangSinh ,GioiTinh ,QuocTich , QueQuan, NoiThuongTruTren, NoiThuongTruDuoi, GiaTriDen = info
        
        # get info
        GiaTriDen_info = GiaTriDen_info_list[random.randint(0,len(GiaTriDen_info_list)-1)]
        GioiTinh_info = GioiTinh_info_list[random.randint(0,1)]
        HoTen_info = HoTen_info_list[random.randint(0,len(HoTen_info_list)-1)]
        NgayThangSinh_info = NgayThangSinh_info_list[random.randint(0,len(NgayThangSinh_info_list)-1)]
        NoiThuongTruTren_info = NoiThuongTruTren_info_list[random.randint(0,len(NoiThuongTruTren_info_list)-1)]
        NoiThuongTruDuoi_info = NoiThuongTruDuoi_info_list[random.randint(0,len(NoiThuongTruDuoi_info_list)-1)]
        QueQuan_info = QueQuan_info_list[random.randint(0,len(QueQuan_info_list)-1)]
        QuocTich_info = "Việt Nam"
        So_info = So_info_list[random.randint(0,len(So_info_list)-1)]

        # set text
        img = Image.open(image_path)
        draw = ImageDraw.Draw(img)
        font_So = ImageFont.truetype("libs/trdg/fonts/latin/ARIALBD.ttf", int(So[3])-3)
        font = ImageFont.truetype("libs/trdg/fonts/latin/ARIAL.ttf", int(GioiTinh[3]))  

        So_info = " ".join(So_info)

        draw.text((int(So[1]),int(So[2])) ,So_info,(180,105,52) ,font=font_So)
        draw.text((int(HoTen[1]),int( HoTen[2])), HoTen_info ,(0,0,0),font=font)
        draw.text((int(NgayThangSinh[1]),int(NgayThangSinh[2]) ),  NgayThangSinh_info ,(0,0,0),font=font)
        draw.text((int(GioiTinh[1]),int( GioiTinh[2])), GioiTinh_info ,(0,0,0),font=font)
        draw.text((int(QuocTich[1]),int(QuocTich[2])), QuocTich_info ,(0,0,0),font=font)
        draw.text((int(NoiThuongTruTren[1]),int(NoiThuongTruTren[2])),  NoiThuongTruTren_info ,(0,0,0),font=font)
        draw.text((int(NoiThuongTruDuoi[1]),int(NoiThuongTruDuoi[2])),  NoiThuongTruDuoi_info ,(0,0,0),font=font)
        draw.text((int(QueQuan[1]),int(QueQuan[2])),  QueQuan_info ,(0,0,0),font=font)
        draw.text((int(GiaTriDen[1]),int(GiaTriDen[2])),  GiaTriDen_info ,(0,0,0),font=font)

        image_dest_path = os.path.join(dest_dir, "opencv_{}_{}.jpg".format(image_name, count))
        img.save(image_dest_path)
        count+=1

if __name__ == '__main__':
    root_dir = 'Label2Gen'
    image_name = 'test'
    image_path = os.path.join(root_dir, image_name + '.png')
    annot_path = os.path.join(root_dir, image_name + '.txt')
    addTextWithOpenCV(image_path, annot_path, image_name)