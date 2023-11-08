import shutil
import cv2
import os
import pandas as pd
import numpy as np


def AOLP2YOLO(txt_in_path, txt_out_path):
    i = 0
    for label in os.listdir(txt_in_path):
        print('label', label)
        with open(txt_in_path+label, 'r', encoding='utf-8') as f:
            points = f.readline()
            print('points:', points)

            lx, ly = lt.split("&", 1)
            rx, ry = rb.split("&", 1)
            width = int(rx) - int(lx)
            height = int(ry) - int(ly)
            cx = float(lx) + width / 2
            cy = float(ly) + height / 2

            img = cv2.imread(imagePath + filename)
            if img is None:
                print('read_error:', os.path.join(imagePath + filename))
                continue
            width = width / img.shape[1]
            height = height / img.shape[0]
            cx = cx / img.shape[1]
            cy = cy / img.shape[0]

            txtname = filename.split(".", 1)
            txtfile = txt_out_path + txtname[0] + ".txt"
            i += 1
            print('num:', i)
            with open(txtfile, "w") as f:
                f.write(str(1) + " " + str(cx) + " " + str(cy) + " " + str(width) + " " + str(height))


if __name__ == '__main__':

    label_path0 = "/data/zxy/datasets/AOLP/Subset_AC/Subset_AC/groundtruth_localization/"
    label_path1 = "/data/zxy/datasets/AOLP/Subset_LE/Subset_LE/groundtruth_localization/"
    label_path2 = "/data/zxy/datasets/AOLP/Subset_RP/Subset_RP/groundtruth_localization/"

    AOLP2YOLO(label_path0, label_path)
