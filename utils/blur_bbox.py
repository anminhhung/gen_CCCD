import cv2 

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
    
def reduce_quality_texture(image, list_of_bbox, param = 50):
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