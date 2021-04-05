
with open("dictionary/NoiThuongTru.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content]

for line in content:
    line = line.split(',')
    with open("dictionary/NoiThuongTruTren.txt", "a+") as f:
        info_tren = line[0] + ',' + line[1]
        f.write("{}\n".format(info_tren))

    with open("dictionary/NoiThuongTruDuoi.txt", "a+") as f1:
        info_duoi = line[2].replace(" ", "")
        f1.write("{}\n".format(line[2]))