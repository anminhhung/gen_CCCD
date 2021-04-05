import os
import random 

with open("dictionary/NgayThangSinh.txt", "a+") as f:
    for i in range(1000):
        date =  random.randint(1, 28)
        month = random.randint(1, 12)
        if date<10:
            date = '0' + str(date)
        else:
            date = str(date)
        
        if month<10:
            month = '0' + str(month)
        else:
            month = str(month)

        date_time = date + '/' + month + '/' + str(random.randint(1945, 2010))
        f.write("{}\n".format(date_time))

with open("dictionary/GiaTriDen.txt", "a+") as f:
    for i in range(1000):
        date =  random.randint(1, 28)
        month = random.randint(1, 12)
        if date<10:
            date = '0' + str(date)
        else:
            date = str(date)
        
        if month<10:
            month = '0' + str(month)
        else:
            month = str(month)

        date_time = date + '/' + month + '/' + str(random.randint(2025, 2050))
        f.write("{}\n".format(date_time))