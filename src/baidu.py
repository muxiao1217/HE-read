import requests
import json
from src.image_process import image_to_base64
import time
import pyautogui
import math


class Baidu():
    def __init__(self):
        self.access_token_url = 'https://aip.baidubce.com/oauth/2.0/token'
        self.app_key = 'UDwerYaq4HHAjs4kpUubQKAM'
        self.app_secret = 'mGentrRE05YYSXor7DrEobCvH3D31y3X'
        self.grant_type = 'client_credentials'
        self.refresh_access_token()

    def refresh_access_token(self):
        params = {
            'grant_type': self.grant_type,
            'client_id': self.app_key,
            'client_secret': self.app_secret
        }
        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
        }
        response = requests.get(self.access_token_url, params=params, headers=headers)
        if response.status_code == 200:
            content = json.loads(response.content, encoding='utf-8')
            self.access_token = content['access_token']

    def read_image_text(self, image):
        url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token={access_token}'.format(
            access_token=self.access_token)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, data={
            'image': image_to_base64(image)
        }, headers=headers)
        print(response.text)
        content = json.loads(response.text)
        pathology_no = ""
        for result in content['words_result']:
            if result['words'].isdigit():
                print(result['words'])
                pathology_no = result['words']
                break
        # result = content['words_result'][1]['words']
        time.sleep(2)
        pyautogui.typewrite(pathology_no + "\n", 0.01)


if __name__ == '__main__':
    baidu = Baidu()
    baidu.read_image_text('')
