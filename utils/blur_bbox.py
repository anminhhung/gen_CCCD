import cv2 
import os 
import numpy as np 

def get_boxes_classes(img_path, anno_path):
    image = cv2.imread(img_path)
    height, width, chanel = image.shape
    colors = np.random.uniform(0, 255, size=(9, 3))
    classes = ['So', 'HoTen', 'NgayThangSinh', 'GioiTinh', 'QuocTich', 'QueQuan', 'NoiThuongTruTren', 'NoiThuongTruDuoi', 'GiaTriDen']

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

def blur_field(image, list_of_bbox):
    '''
      bbox's format: x_min, y_min, x_max, y_max
      list of bbox format: [
        [x_min_0, y_min_0, x_max_0, y_max_0],
        [x_min_1, y_min_1, x_max_1, y_max_1]
        ]
    '''
    for bbox in list_of_bbox:
        field = image[bbox[1] : bbox[3], bbox[0] : bbox[2]]
        field = cv2.blur(field, (5, 5))
        field = cv2.GaussianBlur(field, (5, 5), 100)
        field = cv2.medianBlur(field, 5)
        field = cv2.bilateralFilter(field, 9, 75, 75)
        image[bbox[1] : bbox[3], bbox[0] : bbox[2]] = field

    return image

def reduce_quality_texture(image, list_of_bbox, param=50):
    '''
      bbox format: x_min, y_min, x_max, y_max,
      list_of_bbox format: [
        [x_min_0, y_min_0, x_max_0, y_max_0],
        [x_min_1, y_min_1, x_max_1, y_max_1]
        ]
      param: the smaller value of param, the lower quality of the field
    '''
    for bbox in list_of_bbox:
        field = image[bbox[1] : bbox[3], bbox[0] : bbox[2]]
        field = cv2.resize(field, (param, param))
        field = cv2.resize(field, (bbox[2] - bbox[0], bbox[3] - bbox[1]))
        image[bbox[1] : bbox[3], bbox[0] : bbox[2]] = field

    return image 

if __name__ == '__main__':
    root_dir = "Label2Gen"
    image_name = "test"
    image_path = os.path.join(root_dir, image_name + ".png")
    annot_path = os.path.join(root_dir, image_name + ".txt")

    image, list_bboxes, list_classes = get_boxes_classes(image_path, annot_path)

    # new_image = blur_field(image, list_bboxes)
    new_image = reduce_quality_texture(image, list_bboxes)

    cv2.imshow("image", new_image)
    cv2.waitKey(0)