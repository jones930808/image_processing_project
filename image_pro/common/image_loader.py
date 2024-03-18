# -*- coding: utf-8 -*-
# @Time : 2024-03-18 22:14
# @Author : JoJoMi学习历险记
# @File : image_loader.py
import os
import cv2


class ImageLoader:
    def __init__(self, folder_path):
        """
        初始化图像加载器
        参数：
            folder_path(str): 图像文件夹路径
        :param folder_path:
        """
        self.folder_path = folder_path

    def load_images(self):
        image_files = [f for f in os.listdir(self.folder_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
        # image_count = 0
        images = []
        for image_file in image_files:
            image_path = os.path.join(self.folder_path, image_file)
            image = cv2.imread(image_path)
            if image is not None:
                images.append(image)
        return images

