import base64
import cv2


def image_to_base64(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    s = cv2.imencode('.jpg', image)[1].tostring()
    s = base64.b64encode(s)
    # f1 = open('./1.txt', 'wb')
    # f1.write(s)
    return s


if __name__ == '__main__':
    image_to_base64(cv2.VideoCapture(0).read())
