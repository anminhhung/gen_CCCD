import cv2 
import numpy as np 
import os 
import random
import glob2 
import argparse


from utils.utils import get_boxes_classes, addTextToImage
from utils.addTextWithOpenCV import addTextWithOpenCV

CLASSES = ['So', 'HoTen', 'NgayThangSinh', 'GioiTinh', 'QuocTich', 'QueQuan', 'NoiThuongTruTren', 'NoiThuongTruDuoi', 'GiaTriDen']

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate synthetic text data for text recognition."
    )

    parser.add_argument("--number_gen", type=int,
        help="Number gen_image for each raw image",
        default=10,
    )

    parser.add_argument("--input_dir", type=str,
        help="Input dir (annot & image)",
        default="Label2Gen",
    )

    parser.add_argument("--output_dir", type=str,
        help="Output gen",
        default="gendata",
    )

    return parser.parse_args()

'''
    format image namne: model_<image_name>_<count>.jpg
'''
def gen_with_model(num_gen=10, input_dir="Label2Gen", gen_output="gendata"):
    list_image_path = glob2.glob(os.path.join(input_dir, '*.png'))

    for image_path in list_image_path:
        annot_path = os.path.join(input_dir, (image_path.split("/")[-1]).split(".")[0] + ".txt")
        # raw_image, list_bboxes, list_classes = get_boxes_classes(image_path, annot_path)
        # image_name = (image_path.split("/")[-1]).split(".")[0]

        for cnt in range(num_gen):
            raw_image, list_bboxes, list_classes = get_boxes_classes(image_path, annot_path)
            image_name = (image_path.split("/")[-1]).split(".")[0]
            for (bbox, cls) in zip(list_bboxes, list_classes):
                background_image_path = 'crop_images/{}/{}.png'.format(cls, cls)

                background_image = cv2.imread(background_image_path)

                dest_image = addTextToImage(background_image_path, raw_image, bbox, cls)

            saved_image_name = "model_{}_{}.jpg".format(image_name, cnt)
            cv2.imwrite(os.path.join(gen_output, saved_image_name), dest_image)

'''
    format name: opencv_<image_name>_<count>.jpg
'''
def gen_with_opencv(number_gen=10, input_dir="Label2Gen", gen_output="gendata"):
    list_image_path = glob2.glob(os.path.join(input_dir, '*.png'))

    for image_path in list_image_path:
        image_name = (image_path.split("/")[-1]).split(".")[0]
        annot_path = os.path.join(input_dir, image_name + ".txt")

        addTextWithOpenCV(image_path, annot_path, image_name, number_gen, gen_output)

if __name__ == '__main__':
    # Argument parsing
    args = parse_arguments()

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    gen_with_opencv(args.number_gen, args.input_dir, args.output_dir)
    gen_with_model(args.number_gen, args.input_dir, args.output_dir)