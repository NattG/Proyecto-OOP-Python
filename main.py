import ImageStorage
import ConvertImage


if __name__ == '__main__':
    img = ImageStorage.read_image("Image/koala.jpg")
    img_canny = ConvertImage.img_to_canny_edge_deteccion(img)
    ImageStorage.save_img(img=img_canny, name_img="koala_bordes")
    print("El proyecto corrio exitosamente!!! :D")
