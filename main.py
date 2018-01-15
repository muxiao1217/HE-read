import cv2
from src.baidu import Baidu
import socket


def read():
    camera = cv2.VideoCapture(0)
    success, frame = camera.read()
    baidu = Baidu()
    # frame = cv2.imread('C:/project/code/HE-read/src/1.jpg')
    baidu.read_image_text(frame)
    camera.release()


def create_socket():
    sk = socket.socket()
    sk.bind(("127.0.0.1", 8888))
    sk.listen(5)
    while True:
        conn, _ = sk.accept()
        accept_data = str(conn.recv(1024),
                          encoding="utf8")
        print(accept_data)
        if accept_data == '200':
            read()
        print(accept_data)


if __name__ == '__main__':
    print('read start')
    create_socket()
