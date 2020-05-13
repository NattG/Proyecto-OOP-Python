import cv2


class ImageStorage:


 @classmethod
 def read_image(path_img):
        if isinstance(path_img, str):
            img = cv2.imread(path_img)
            return img
        else:
            print("formato no valido")
            return None
 @classmethod
 def save_img(img, name_img):
    name_img = name_img + ".jpg"
    cv2.imwrite(name_img, img)


def read_image(path_img):
    if isinstance(path_img, str):
        img = cv2.imread(path_img)
        return img
    else:
        print("formato no valido")
        return None


def save_img(img, name_img):
    name_img = name_img + ".jpg"
    cv2.imwrite(name_img, img)