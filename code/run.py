import os
import cv2
import glob
from pil import Image
from pil import ImageFont
from pil import ImageDraw 
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

def convert(annot_path):   
    term=[]
    img_path = annot_path.split(".")[0]+".jpg" 
    img_path = str(img_path.replace("\\","/"))
    
    img = cv2.imread(img_path)
    
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
        

###############
print("----------------------gen----------------------")

if os.path.exists("data")==False:
    os.mkdir("data")

#search background
backgrounds = []
for i in glob.glob("background/*.txt"):
    i =i .split(".")[0].replace("\\","/")
    backgrounds.append(i)

# Get dict
GiaTriDen_info_list = open("dict/GiaTriDen.txt",encoding = 'utf-8').readlines()
GioiTinh_info_list = open("dict/GioiTinh.txt",encoding = 'utf-8').readlines()
HoTen_info_list = open("dict/HoTen.txt",encoding = 'utf-8').readlines()
NgayThangSinh_info_list = open("dict/NgayThangSinh.txt",encoding = 'utf-8').readlines()
NoiThuongTru1_info_list = open("dict/NoiThuongTru1.txt",encoding = 'utf-8').readlines()
NoiThuongTru2_info_list = open("dict/NoiThuongTru2.txt",encoding = 'utf-8').readlines()
QueQuan_info_list = open("dict/QueQuan.txt",encoding = 'utf-8').readlines()
QuocTich_info_list = open("dict/QuocTich.txt",encoding = 'utf-8').readlines()
So_info_list = open("dict/So.txt",encoding = 'utf-8').readlines()

count=0
for _ in tqdm(range(100)):
    #get background in list
    background = backgrounds[random.randint(0,len(backgrounds)-1)]
    info = convert(background+".txt")
    
    So, HoTen,NgayThangSinh ,GioiTinh ,QuocTich , QueQuan, NoiThuongTru1,NoiThuongTru2, GiaTriDen = info
    
    # get info
    GiaTriDen_info = GiaTriDen_info_list[random.randint(0,len(GiaTriDen_info_list)-1)]
    GioiTinh_info = GioiTinh_info_list[random.randint(0,1)]
    HoTen_info = HoTen_info_list[random.randint(0,len(HoTen_info_list)-1)]
    NgayThangSinh_info = NgayThangSinh_info_list[random.randint(0,len(NgayThangSinh_info_list)-1)]
    NoiThuongTru1_info = NoiThuongTru1_info_list[random.randint(0,len(NoiThuongTru1_info_list)-1)]
    NoiThuongTru2_info = NoiThuongTru2_info_list[random.randint(0,len(NoiThuongTru2_info_list)-1)]
    QueQuan_info = QueQuan_info_list[random.randint(0,len(QueQuan_info_list)-1)]
    QuocTich_info ="Việt Nam"
    So_info = So_info_list[random.randint(0,len(So_info_list)-1)]
    

    # set text

    img = Image.open(background+".jpg")
    draw = ImageDraw.Draw(img)
    font_So = ImageFont.truetype("font/ARIALNB.TTF", int(So[3])-3)
    font = ImageFont.truetype("font/ARIAL.TTF", int(GioiTinh[3]))
    

    So_info = " ".join(So_info)

    draw.text((int(So[1]),int(So[2])) ,So_info,(180,105,52) ,font=font_So)
    draw.text((int(HoTen[1]),int( HoTen[2])),  HoTen_info ,(0,0,0),font=font)
    draw.text((int(NgayThangSinh[1]),int(NgayThangSinh[2]) ),  NgayThangSinh_info ,(0,0,0),font=font)
    draw.text((int(GioiTinh[1]),int( GioiTinh[2])),  GioiTinh_info ,(0,0,0),font=font)
    draw.text((int(QuocTich[1]),int(QuocTich[2])),  QuocTich_info ,(0,0,0),font=font)
    draw.text((int(NoiThuongTru1[1]),int( NoiThuongTru1[2])),  NoiThuongTru1_info ,(0,0,0),font=font)
    draw.text((int(NoiThuongTru2[1]),int( NoiThuongTru2[2])),  NoiThuongTru2_info ,(0,0,0),font=font)
    draw.text((int(QueQuan[1]),int(QueQuan[2]) ),  QueQuan_info ,(0,0,0),font=font)
    draw.text((int(GiaTriDen[1]),int(GiaTriDen[2]) ),  GiaTriDen_info ,(0,0,0),font=font)
    img.save('data/data'+str(count)+".jpg")
    count+=1
    

