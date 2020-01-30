import os
import json
import base64
import re

from django.http.request import QueryDict
from django.utils.six import StringIO

from channels.generic.websocket import WebsocketConsumer

from ..ssh import SSH


class WebSSH(WebsocketConsumer):
    message = {'status': 0, 'message': None}
    """
    status:
        0: ssh 连接正常, websocket 正常
        1: 发生未知错误, 关闭 ssh 和 websocket 连接

    message:
        status 为 1 时, message 为具体的错误信息
        status 为 0 时, message 为 ssh 返回的数据, 前端页面将获取 ssh 返回的数据并写入终端页面
    """

    def connect(self):
        """
        打开 websocket 连接, 通过前端传入的参数尝试连接 ssh 主机
        :return:
        """
        self.accept()
        query_string = self.scope.get('query_string')
        ssh_args = QueryDict(query_string=query_string, encoding='utf-8')

        width = ssh_args.get('width')
        height = ssh_args.get('height')

        width = int(width)
        height = int(height)

        user = ssh_args.get('user')

        self.ssh = SSH(websocker=self, message=self.message)

        ssh_connect_dict = {
            'host': '10.12.31.20',
            'user': 'uclv_victor',
            'port': 22,
            'timeout': 30,
            'pty_width': width,
            'pty_height': height,
            'password': '12345*abc'
        }

        # if auth == 'key':
        #     ssh_key_file = os.path.join(TMP_DIR, ssh_key_name)
        #     with open(ssh_key_file, 'r') as f:
        #         ssh_key = f.read()
        #
        #     string_io = StringIO()
        #     string_io.write(ssh_key)
        #     string_io.flush()
        #     string_io.seek(0)
        #     ssh_connect_dict['ssh_key'] = string_io
        #
        #     os.remove(ssh_key_file)

        self.ssh.connect(**ssh_connect_dict)

    def disconnect(self, close_code):
        try:
            if close_code == 3001:
                pass
            else:
                self.ssh.close()
        except:
            pass
        finally:
            # Filtrar caracteres de color en resultados de puntos
            res = re.sub('(\[\d{2};\d{2}m|\[0m)', '', self.ssh.res)
            print('命令: ')
            print(self.ssh.cmd)
            print('结果: ')
            print(res)

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        if type(data) == dict:
            status = data['status']
            if status == 0:
                data = data['data']
                self.ssh.shell(data)
            else:
                cols = data['cols']
                rows = data['rows']
                self.ssh.resize_pty(cols=cols, rows=rows)
