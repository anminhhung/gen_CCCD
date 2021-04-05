import os
import glob
from pil import Image
from pil import ImageFont
from pil import ImageDraw 
import random 
from tqdm import tqdm
if os.path.exists("data")==False:
    os.mkdir("data")

#search background
backgrounds = []
for i in glob.glob("background/*.txt"):
    i =i .split(".")[0].replace("\\","/")
    backgrounds.append(i)

GiaTriDen_info_a = open("dict/GiaTriDen.txt",encoding = 'utf-8').readlines()
GioiTinh_info_a = open("dict/GioiTinh.txt",encoding = 'utf-8').readlines()
HoTen_info_a = open("dict/HoTen.txt",encoding = 'utf-8').readlines()
NgayThangSinh_info_a = open("dict/NgayThangSinh.txt",encoding = 'utf-8').readlines()
NoiThuongTru1_info_a = open("dict/NoiThuongTru1.txt",encoding = 'utf-8').readlines()
NoiThuongTru2_info_a = open("dict/NoiThuongTru2.txt",encoding = 'utf-8').readlines()
QueQuan_info_a = open("dict/QueQuan.txt",encoding = 'utf-8').readlines()
QuocTich_info_a = open("dict/QuocTich.txt",encoding = 'utf-8').readlines()
So_info_a = open("dict/So.txt",encoding = 'utf-8').readlines()

count=0
for _ in tqdm(range(100)):
    background = backgrounds[random.randint(0,len(backgrounds)-1)]

    info  = open(background+".txt", 'r')
    info = info.readlines()
    for i in range(len(info)):
        info[i]=info[i].replace("\n","")
        
    So, HoTen,NgayThangSinh ,GioiTinh ,QuocTich , QueQuan, NoiThuongTru1,NoiThuongTru2, GiaTriDen = info
    
    ####### get info
    GiaTriDen_info = GiaTriDen_info_a[random.randint(0,len(backgrounds)-1)]
    GioiTinh_info = GioiTinh_info_a[random.randint(0,1)]
    HoTen_info = HoTen_info_a[random.randint(0,len(backgrounds)-1)]
    NgayThangSinh_info = NgayThangSinh_info_a[random.randint(0,len(backgrounds)-1)]
    NoiThuongTru1_info = NoiThuongTru1_info_a[random.randint(0,len(backgrounds)-1)]
    NoiThuongTru2_info = NoiThuongTru2_info_a[random.randint(0,len(backgrounds)-1)]
    QueQuan_info = QueQuan_info_a[random.randint(0,len(backgrounds)-1)]
    QuocTich_info ="Việt Nam"
    So_info = So_info_a[random.randint(0,len(backgrounds)-1)]
    #######
    
    
    GiaTriDen = str(GiaTriDen).split(" ")
    GioiTinh = str(GioiTinh).split(" ")
    HoTen = str(HoTen).split(" ")
    NgayThangSinh = str(NgayThangSinh).split(" ")
    NoiThuongTru1 = str(NoiThuongTru1).split(" ")
    NoiThuongTru2 = str(NoiThuongTru2).split(" ")
    QueQuan = str(QueQuan).split(" ")
    QuocTich = str(QuocTich).split(" ")
    So = So.split(" ")



    img = Image.open(background+".jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font\ARIAL.TTF", int(GioiTinh[3]))
    font_So = ImageFont.truetype("font\ARIALNB.TTF", int(So[3]))

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
    break

