#!/usr/bin/python3
# encoding=utf8

import requests
import sys

URL = 'http://fanyi.youdao.com/openapi.do'


class Youdao():
    def __init__(self):
        if sys.argv.__len__() > 1:
            txt = sys.argv[1] + ''
            resp = requests.post(URL, {
                'keyfrom': 'ppwangs',
                'key': '359440176',
                'type': 'data',
                'doctype': 'json',
                'version': '1.1',
                'q': txt})
            self._parse(resp.json(), txt)

    def _parse(self, response, txt):
        # str = txt
        # str = txt
        if response and response['errorCode'] == 0:
            # str += '：\r'
            str = '';
            if 'basic' in response and response['basic'] != {}:
                str += '{} - 基本词义：\r'.format(txt)
                str += '        ' + '; \r        '.join(response['basic']['explains'])

            if 'web' in response and response['web'] != []:
                if str.__len__() > 0:
                    str += '\r'
                str += '{} - 网络扩展：\r'.format(txt)
                for web in response['web']:
                    str += '        ' + web['key'] + ': ' + '; '.join(web['value']) + '\r'

            if str.__len__() > 0:
                str += '----------------------------------------------------------------------------'
                print(str)

            if 'translation' in response and response['translation'] != []:
                print('; '.join(response['translation']))

        elif response:
            code = response['errorCode']
            msg = '未知错误'

            if code == 20:
                msg = '要翻译的文本过长'
            elif code == 30:
                msg = '无法进行有效的翻译'
            elif code == 40:
                msg = '不支持的语言类型'
            elif code == 50:
                msg = '无效的key'
            elif code == 60:
                msg = '无词典结果'
            else:
                pass
            print(msg)

        else:
            pass


if __name__ == '__main__':
    Youdao()
