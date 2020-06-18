"""check parameters"""
import os
import cv2
import numpy as np
import imghdr


def area_rect(bbox):
    """ determine the area of a bbox"""
    x=int(bbox[2])-int(bbox[0])
    y=int(bbox[3])-int(bbox[1])
    return x*y


def check_vectors(v1,v2):
    """check vectors"""
    try:
        if len(v1)!= 1000 or len(v2)!=1000:
            raise Exception( 'Dimension of the vector not valid')
    except TypeError:
        raise Exception('TypeError')
    else:
        return 'true'


def check_bbox(bb):
    """check bounding box"""
    bbox = []
    bbox.append(bb['coordinate_x'])
    bbox.append(bb['coordinate_y'])
    bbox.append(bb['width'])
    bbox.append(bb['height'])
    return bbox


def category_present(image_path, box):
    """ check if category provided is present"""

    if len(box) == 0 or len(box) > 4:
        raise Exception('bbox_error')

    if not os.path.isfile(image_path):
        raise Exception("path_error")

    if os.path.isfile(str(image_path)):
        status = is_image(image_path)
        if status != 1:
            return 'false'
        img = cv2.imread(image_path)
        height = np.size(img, 0)
        width = np.size(img, 1)
        size=height*width
        if size < 784:
            raise Exception('query image is too small')
        if len(box)!= 0:
            area = area_rect(box)
            if area > size:
                raise Exception( 'Selected query size is greater then the image')
            if area < 784:
                raise Exception('Selected image is too small to process')
    return 'true'


def is_image(im_name):
    """check if the path has image"""
    status = 0
    lis = ['jpeg','bmp','jpg','png','tiff']
    if imghdr.what(im_name) is None:
        status = -1
    if imghdr.what(im_name) in lis:
        status = 1
    return status
