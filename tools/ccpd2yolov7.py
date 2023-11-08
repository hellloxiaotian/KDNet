import shutil
import cv2
import os

imagePath = "/data/zxy/datasets/CCPD2019/"


def txt_translate(path, txt_path):
    i = 0
    for filename in os.listdir(path):
        list1 = filename.split("-", 3)
        subname = list1[2]
        list2 = filename.split(".", 1)
        subname1 = list2[1]
        if subname1 == 'txt':
            continue
        lt, rb = subname.split("_", 1)
        lx, ly = lt.split("&", 1)
        rx, ry = rb.split("&", 1)
        width = int(rx) - int(lx)
        height = int(ry) - int(ly)
        cx = float(lx) + width / 2
        cy = float(ly) + height / 2

        img = cv2.imread(path + filename)
        if img is None:
            print('read_error:', os.path.join(path, filename))
            continue
        width = width / img.shape[1]
        height = height / img.shape[0]
        cx = cx / img.shape[1]
        cy = cy / img.shape[0]

        txtname = filename.split(".", 1)
        txtfile = txt_path + txtname[0] + ".txt"
        i += 1
        print('num:', i)
        with open(txtfile, "w") as f:
            f.write(str(1) + " " + str(cx) + " " + str(cy) + " " + str(width) + " " + str(height))


def splits_translate(path, txt_path):
    i = 0
    for filename in os.listdir(path):
        pathname = path.split("/", -1)[-2]
        print('pathname:', pathname)
        txtfile = txt_path + pathname + ".txt"
        print('txtfile:', txtfile)
        i += 1
        print('num:', i)
        with open(txtfile, "a") as f:
            f.write(pathname + "/" + filename + '\n')

if __name__ == '__main__':
    baseDir = "/data/zxy/datasets/CCPD2019/images/ccpd_base/"
    blurDir = "/data/zxy/datasets/CCPD2019/ccpd_blur/"
    challengeDir = "/data/zxy/datasets/CCPD2019/ccpd_challenge/"
    dbDir = "/data/zxy/datasets/CCPD2019/ccpd_db/"
    fnDir = "/data/zxy/datasets/CCPD2019/ccpd_fn/"
    npDir = "/data/zxy/datasets/CCPD2019/ccpd_np/"
    rotateDir = "/data/zxy/datasets/CCPD2019/ccpd_rotate/"
    tiltDir = "/data/zxy/datasets/CCPD2019/ccpd_tilt/"
    weatherDir = "/data/zxy/datasets/CCPD2019/ccpd_weather/"

    test_path0 = "/data/zxy/datasets/CCPD2019/labels/ccpd_base/"
    test_path = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_blur/"
    test_path1 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_challenge/"
    test_path2 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_db/"
    test_path3 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_fn/"
    test_path4 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_np/"
    test_path5 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_rotate/"
    test_path6 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_tilt/"
    test_path7 = "/data/zxy/datasets/CCPD2019/splits/labels/ccpd_weather/"

    split_path = "/data/zxy/datasets/CCPD2019/splits/"

    train_txt_path = "/data/zxy/datasets/CCPD2019/splits/train.txt"
    val_txt_path = "/data/zxy/datasets/CCPD2019/splits/val.txt"
    test_txt_path = "/data/zxy/datasets/CCPD2019/splits/test.txt"

    label_train_txt_path = "/data/zxy/datasets/CCPD2019/splits/labels/train/"
    label_val_txt_path = "/data/zxy/datasets/CCPD2019/splits/labels/val/"
    label_test_txt_path = "/data/zxy/datasets/CCPD2019/splits/labels/test/"

    # txt_translate(baseDir, test_path0)
    # txt_translate(testDir, test_path)
    # txt_translate(challengeDir, test_path1)
    # txt_translate(dbDir, test_path2)
    # txt_translate(fnDir, test_path3)
    # txt_translate(npDir, test_path4)
    # txt_translate(rotateDir, test_path5)
    # txt_translate(tiltDir, test_path6)
    # txt_translate(weatherDir, test_path7)

    splits_translate(weatherDir, split_path)

    # txt_translate_txt(train_txt_path, label_train_txt_path)
    # txt_translate_txt(test_txt_path, label_test_txt_path)
    # txt_translate_txt(val_txt_path, label_val_txt_path)

    # txt_translate(trainDir, train_txt_path)
    # txt_translate(validDir, val_txt_path)
    # txt_translate(testDir, test_txt_path)
