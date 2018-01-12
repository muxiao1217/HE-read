import cv2
import pyHook
from src.baidu import Baidu


def read():
    camera = cv2.VideoCapture(0)
    success, frame = camera.read()
    baidu = Baidu()
    # frame = cv2.imread('C:/project/code/HE-read/src/1.jpg')
    baidu.read_image_text(frame)
    camera.release()


def keyboard_event(event):
    print(event)
    key = event.Key
    if key == 'F8':
        read()
    return True


if __name__ == '__main__':
    import pythoncom

    print("已启动")
    hm = pyHook.HookManager()
    hm.HookKeyboard()
    hm.KeyDown = keyboard_event
    pythoncom.PumpMessages()
