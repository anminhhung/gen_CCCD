import cv2 
import numpy as np 
import os 
import random
import glob2 

from utils.utils import get_boxes_classes, add_background_with_text_to_raw_image

CLASSES = ['So', 'HoTen', 'NgayThangSinh', 'GioiTinh', 'QuocTich', 'QueQuan', 'NoiThuongTru', 'GiaTriDen']

if __name__ == '__main__':
    gen_output = "gendata"

    if not os.path.exists(gen_output):
        os.mkdir(gen_output)

    list_image_path = glob2.glob(os.path.join('Label2Gen', '*.jpg'))

    for image_path in list_image_path:
        annot_path = os.path.join("Label2Gen", (image_path.split("/")[-1]).split(".")[0] + ".txt")
        raw_image, list_bboxes, list_classes = get_boxes_classes(image_path, annot_path)
        image_name = image_path.split("/")[-1]
        for (bbox, cls) in zip(list_bboxes, list_classes):
            background_image_path = 'crop_images/{}/{}.png'.format(cls, cls)

            background_image = cv2.imread(background_image_path)

            raw_image = add_background_with_text_to_raw_image(background_image, background_image_path, raw_image, bbox, cls)

        cv2.imwrite(os.path.join(gen_output, image_name), raw_image)