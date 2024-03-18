# -*- coding: utf-8 -*-
# @Time : 2024-03-18 22:26
# @Author : JoJoMi学习历险记
# @File : main.py

import cv2
from image_pro.common import image_loader


def main():
    loader = image_loader.ImageLoader('image_pro/data/input')

    images = loader.load_images()

    for image in images:
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



if __name__ == '__main__':
    main()

