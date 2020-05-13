import cv2

class ConverImage:

 @classmethod
 def img_to_canny_edge_deteccion(img):
    canny_img = cv2.Canny(img, 100, 200)
    return canny_img


def img_to_canny_edge_deteccion(img):
    canny_img = cv2.Canny(img, 100, 200)
    return canny_img