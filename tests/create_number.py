import random

with open("dictionary/So.txt", "a+") as f:
    for i in range(1000):
        tmp = ''
        for j in range(12):
            tmp += str(random.randint(0, 9))
        f.write("{}\n".format(tmp))