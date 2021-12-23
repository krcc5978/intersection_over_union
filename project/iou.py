import numpy as np


def intersection_over_union(a, b):
    # get area of a
    area_a = (a[2] - a[0]) * (a[3] - a[1])
    # get area of b
    area_b = (b[2] - b[0]) * (b[3] - b[1])

    # ratio = area_a / area_b

    # get left top x of IoU
    iou_x1 = np.maximum(a[0], b[0])
    # get left top y of IoU
    iou_y1 = np.maximum(a[1], b[1])
    # get right bottom of IoU
    iou_x2 = np.minimum(a[2], b[2])
    # get right bottom of IoU
    iou_y2 = np.minimum(a[3], b[3])

    # get width of IoU
    iou_w = iou_x2 - iou_x1
    # get height of IoU
    iou_h = iou_y2 - iou_y1

    # no overlap
    if iou_w < 0 or iou_h < 0:
        return 0

    # get area of IoU
    area_iou = iou_w * iou_h
    # get overlap ratio between IoU and all area
    iou = area_iou / (area_a + area_b - area_iou)

    a_overlap = area_iou/area_a
    b_overlap = area_iou/area_b
    print(f'a_overlap : {a_overlap}')
    print(f'b_overlap : {b_overlap}')

    # if ratio < 1:
    #     iou = iou / ratio
    # else:
    #     iou = iou * ratio

    print(f'iou : {iou}')

    return max((iou,a_overlap,b_overlap))

