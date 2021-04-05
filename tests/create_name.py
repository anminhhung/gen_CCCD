import os
import random 

LIST_FIRST_NAME = ['An', 'Nguyễn', 'Trần', 'Phạm', 'Mai', 'Hồ', 'Đinh', 'Phạm', 'Lợi', 'A']
LIST_MID_NAME = ['Thị', 'Anh', 'Hồng', 'Minh', 'Quang', 'Hữu', 'Công', 'Trung', 'Xuân']
List_LAST_NAME = ['Hùng', 'Linh', 'Quang', 'Hiếu', 'Trung', 'Thái', 'Cường', 'Kiên', 'Dũng',\
    'Khiêm', 'Quế', 'Chiến', 'An', 'Thái', 'Công', 'Trường', 'Thịnh', 'Xuân', 'Mai', 'Hải', \
    'Tiến', 'Trang', 'Trịnh', 'Đào']

with open("dictionary/HoTen.txt", "a+") as f:
    for i in range(1000):
        name = random.choice(LIST_FIRST_NAME) + ' ' + random.choice(LIST_MID_NAME) + ' ' + random.choice(List_LAST_NAME)
        f.write("{}\n".format(name))