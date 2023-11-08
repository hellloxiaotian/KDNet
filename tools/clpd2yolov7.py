import shutil
import cv2
import os
import pandas as pd
import numpy as np

imagePath = "/data/zxy/datasets/CLPD/"
labelPath = "/data/zxy/datasets/CLPD/splits/labels/"


def CLPD2YOLO(csv_path):
    clpd = pd.read_csv(csv_path, encoding="utf-8")
    clpd = np.array(clpd)
    clpd = clpd.tolist()
    for list in clpd:
        image = list[0]  # CLPD_1200/1199.jpg
        lux = list[1]  # left upper x
        luy = list[2]  # left upper y
        rux = list[3]
        ruy = list[4]
        rdx = list[5]  # right down x
        rdy = list[6]  # right down y
        ldx = list[7]
        ldy = list[8]
        if lux < ldx:
            lx = lux
        else:
            lx = ldx
        if luy < ruy:
            ly = luy
        else:
            ly = ruy
        if rux < rdx:
            rx = rdx
        else:
            rx = rux
        if ldy < rdy:
            ry = rdy
        else:
            ry = ldy
        width = int(rx) - int(lx)
        height = int(ry) - int(ly)
        cx = float(lx) + width / 2
        cy = float(ly) + height / 2

        img = cv2.imread(imagePath + image)
        if img is None:
            print('read_error:', os.path.join(csv_path + image))
            continue
        width = width / img.shape[1]
        height = height / img.shape[0]
        cx = cx / img.shape[1]
        cy = cy / img.shape[0]
        txtfile = labelPath + image.split("/", 1)[1].split(".", 1)[0] + ".txt"
        print('txtfile:', txtfile)
        with open(txtfile, "w") as f:
            f.write(str(1) + " " + str(cx) + " " + str(cy) + " " + str(width) + " " + str(height))


if __name__ == '__main__':
    csv_path = "/data/zxy/datasets/CLPD/CLPD.csv"

    CLPD2YOLO(csv_path)