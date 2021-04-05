import cv2 
import os
import numpy as np

def get_boxes_classes(img_path, anno_path):
    image = cv2.imread(img_path)
    height, width, chanel = image.shape
    colors = np.random.uniform(0, 255, size=(8, 3))
    classes = ['So', 'HoTen', 'NgayThangSinh', 'GioiTinh', 'QuocTich', 'QueQuan', 'NoiThuongTru', 'GiaTriDen']

    with open(anno_path) as f:
        boxes = f.read().split('\n')

    list_bboxes = []
    list_classes = []

    for box in boxes:
        if len(box)==0:
            continue
        cls = int(box.split()[0])
        xc = int(float(box.split()[1]) * width)
        yc = int(float(box.split()[2]) * height)
        w = int(float(box.split()[3]) * width)
        h = int(float(box.split()[4]) * height)

        xmin = xc - w//2
        ymin = yc - h//2
        xmax = xmin + w
        ymax = ymin + h

        list_bboxes.append([xmin, ymin, xmax, ymax])
        list_classes.append(classes[cls])

        # image = cv2.rectangle(image, (xmin,ymin), (xmax,ymax), colors[cls])
        # image = cv2.putText(image, classes[cls], (xmin, ymin), cv2.FONT_HERSHEY_PLAIN, 1, colors[cls], 2)

    return image, list_bboxes, list_classes

'''
    bbox: formax max-min (list of value)
    [xmin, ymin, xmax, ymax]
'''
def add_background_with_text_to_raw_image(background_image, background_image_path, raw_image, bbox, cls):
    is_neg = False 
    delta = None 

    background_image = cv2.resize(background_image, (bbox[2] - bbox[0], bbox[3] - bbox[1]))
    background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(background_image)
    v_histogram = cv2.calcHist([v], [0], None, [256], [0, 256])
    elem_v_histogram_background = np.argmax(v_histogram)

    # get image from bbox
    image_from_bbox = raw_image[bbox[1] : bbox[3], bbox[0] : bbox[2]]
    image_from_bbox = cv2.cvtColor(image_from_bbox, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image_from_bbox)
    v_histogram = cv2.calcHist([v], [0], None, [256], [0, 256])
    elem_v_histogram_bbox = np.argmax(v_histogram)
    
    tmp = elem_v_histogram_bbox - elem_v_histogram_background
    if tmp < 0:
        is_neg = True 
        delta = abs(tmp)
    else:
        delta = tmp

    if is_neg == True:
        background_image[:, :, 2] -= delta
    else:
        background_image[:, :, 2] += delta
    
    background_image = cv2.cvtColor(background_image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(background_image_path, background_image)


    # add text
    if cls != 'So':
        os.system("python3 trdg/run.py -c 1 -w 1 -f 40 -l vi -b --dict dictionary/{}.txt --image_dir crop_images/{} --output_dir gen_text_results/{}".format(cls, cls, cls))
    else:
        os.system("python3 trdg/run.py -c 1 -w 1 -f 40 -l vi -b --dict dictionary/So.txt --image_dir crop_images/So --output_dir gen_text_results/So --text_color '#ff0000,#e50000'")

    f = open("gen_text_results/info.txt", "r")
    background_with_text_image_path = f.read()

    background_with_text_image = cv2.imread(background_with_text_image_path)
    background_with_text_image = cv2.resize(background_with_text_image, (bbox[2] - bbox[0], bbox[3] - bbox[1]))

    raw_image[bbox[1] : bbox[3], bbox[0] : bbox[2]] = background_with_text_image

    return raw_image

# def add_background_with_text_to_raw_image(background_image, background_with_text_image, raw_image, bbox):
#     is_neg = False 
#     delta = None 

#     background_image = cv2.resize(background_image, (bbox[2] - bbox[0], bbox[3] - bbox[1]))
#     background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2HSV)
#     h, s, v = cv2.split(background_image)
#     v_histogram = cv2.calcHist([v], [0], None, [256], [0, 256])
#     elem_v_histogram_background = np.argmax(v_histogram)

#     # get image from bbox
#     image_from_bbox = raw_image[bbox[1] : bbox[3], bbox[0] : bbox[2]]
#     image_from_bbox = cv2.cvtColor(image_from_bbox, cv2.COLOR_BGR2HSV)
#     h, s, v = cv2.split(image_from_bbox)
#     v_histogram = cv2.calcHist([v], [0], None, [256], [0, 256])
#     elem_v_histogram_bbox = np.argmax(v_histogram)
    
#     tmp = elem_v_histogram_bbox - elem_v_histogram_background
#     if tmp < 0:
#         is_neg = True 
#         delta = abs(tmp)
#     else:
#         delta = tmp

#     background_with_text_image = cv2.resize(background_with_text_image, (bbox[2] - bbox[0], bbox[3] - bbox[1]))
#     background_with_text_image = cv2.cvtColor(background_with_text_image, cv2.COLOR_BGR2HSV)
#     cv2.imshow("background image before +- delta", background_with_text_image)
#     if is_neg == True:
#         background_with_text_image[:, :, 2] -= delta
#     else:
#         background_with_text_image[:, :, 2] += delta
    
#     background_with_text_image = cv2.cvtColor(background_with_text_image, cv2.COLOR_HSV2BGR)
#     cv2.imshow("background image after +- delta", background_with_text_image)
#     raw_image[bbox[1] : bbox[3], bbox[0] : bbox[2]] = background_with_text_image

#     return raw_image

if __name__ == '__main__':
    root_dir = "Label2Gen"
    image_name = "CCCD0"
    image_path = os.path.join(root_dir, image_name + ".jpg")
    annot_path = os.path.join(root_dir, image_name + ".txt")

    image, list_bboxes, list_classes = get_boxes_classes(image_path, annot_path)
    cv2.imshow("image", image)
    cv2.waitKey(0)