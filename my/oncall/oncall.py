#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# oncall.py - capture chrome input, gather info from ssh, then send to weixin-work

# Date   : 2020/12/09
import logging
import requests
import base64
import hashlib
import json
import os
import time

# pip3 install chromedriver-binary-auto selenium paramiko pillow
try:
    import paramiko
    import chromedriver_binary
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from PIL import Image, ImageFont, ImageDraw
except Exception as e:
    print('pip3 install chromedriver-binary-auto selenium paramiko pillow')
    raise(e)

logger = logging.getLogger('abc')
weixin_url = 'https://qyapi.weixin.qq.com'
robot_key = 'f3ee8839-f66c-4470-a36d-465b7562b306'
weekday = ['一', '二', '三', '四', '五', '六', '日']

class OnCall:
    def __init__(self, basedir, debug=False):
        self.debug = debug
        self.basedir = basedir
        self.weixin_robot_url = "{}/cgi-bin/webhook/send?key={}".format(weixin_url, robot_key)
        self.weixin_media_id_url = "{}/cgi-bin/webhook/upload_media?key={}&type=file".format(weixin_url, robot_key)

    def capture_images(self):
        logger.debug('capture_images')
        username = 'yshi@addx.ai'
        password = '19910310lang+'
        grafana = 'http://grafana.addx.live'

        try:
            chrome_options = Options().add_argument('headless')
            brower = webdriver.Chrome(chrome_options=chrome_options)
            logger.debug('chrome started')

            # login
            login = {'uri': 'login', 'name': 'login'}
            url = '{}/{}'.format(grafana, login['uri'])
            logger.debug('open {}'.format(url))
            brower.get(url)
            brower.find_element_by_name('user').clear()
            brower.find_element_by_name('user').send_keys(username)
            brower.find_element_by_name('password').clear()
            brower.find_element_by_name('password').send_keys(password)
            brower.find_element_by_class_name('login-button-group').find_element_by_tag_name('button').click()
            brower.maximize_window()

            # backend
            backend = {'uri': 'd/UWulzimMk/hou-duan?orgId=1&from=now-2d&to=now', 'name': 'backend'}
            url = '{}/{}'.format(grafana, backend['uri'])
            logger.debug('open {}'.format(url))
            brower.get(url)
            time.sleep(3)
            x = brower.find_element_by_id('panel-79')
            brower.execute_script('arguments[0].scrollIntoView();', x)
            time.sleep(5)
            fn = os.path.join(self.basedir, backend['name']) + '.png'
            brower.save_screenshot(fn)
            logger.debug('{} captured'.format(backend['name']))
            self.send_image_weixin(self.weixin_robot_url, fn)

            # ai nodes
            urls = [
                {'uri':'d/9CWBz0bi3/ou-zhou-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-eu-gpu-node2', 'name': 'eu-node2'},
                {'uri': 'd/9CWBz0bil/mei-guo-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-us-gpu-node4', 'name': 'us-node4'},
                {'uri': 'd/9CWBz0bil/mei-guo-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-us-gpu-node5', 'name': 'us-node5'},
            ]
            for x in urls:
                url = '{}/{}'.format(grafana, x['uri'])
                logger.debug('open {}'.format(url))
                brower.get(url)
                time.sleep(8)
                fn = os.path.join(self.basedir, x['name']) + '.png'
                brower.save_screenshot(fn)
                logger.debug('{} captured'.format(x['name']))
                self.send_image_weixin(self.weixin_robot_url, fn)

            brower.close()
            brower.quit()
            logger.debug('capture done')

        except Exception as e:
            brower.quit()
            logger.error(e)
            raise(e)

    def _ssh_shell_recv(self, s):
        buf = ''
        while True:
            r = s.recv(9999)
            r = str(r, encoding='utf-8')
            buf += r
            if r.endswith('# ') or r.endswith('$ '):
                break
        return buf


    def get_payload(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jump = {
            'host':'52.80.136.41',
            'username': 'ec2-user',
            'port': 32222,
            'key':os.path.join(os.getcwd(), 'id_rsa'),
            'name': 'jump'
        }
        hosts = [
            {
                'host': '10.100.2.89',
                'username': 'ubuntu',
                'port': 32222,
                'key': None,
                'jump': jump,
                'name': 'us-1'
            },
            {
                'host': '10.100.2.153',
                'username': 'ubuntu',
                'port': 32222,
                'key': None,
                'jump': jump,
                'name': 'us-2'
            },
            {
                'host': '10.160.1.73',
                'username': 'ubuntu',
                'port': 32222,
                'key': None,
                'jump': jump,
                'name': 'ou-1'
            },
            {
                'host': '52.81.37.85',
                'username': 'ubuntu',
                'port': 32222,
                'key': os.path.join('./', 'id_rsa'),
                'jump': None,
                'name': 'china-1'
            },
        ]

        try:
            # 跳板机
            ssh.connect(hostname=jump['host'],
                        port=jump['port'],
                        username=jump['username'],
                        key_filename=jump['key'])
            s = ssh.invoke_shell()
            s.send('sudo su -\n')
            r = self._ssh_shell_recv(s)
            logger.debug('login jump {}@{}'.format(jump['username'], jump['host']))
            # logger.debug(r)

            for x in hosts:
                if x['jump'] == jump:
                    logger.debug('ssh {} {}@{}'.format(x['name'], x['username'], x['host']))
                    s.send("ssh -p{} {}@{} 'hostname; ps aux | grep python | grep -v grep'\r\n".format(
                        x['port'], x['username'], x['host']))
                    r = self._ssh_shell_recv(s)
                    fn = os.path.join(self.basedir, x['name']) + '.txt'

                    # logger.debug(r)
                    with open(fn, 'w') as f:
                        f.write(r)
                    logger.debug("{} get_payload".format(x['name']))
                    self.convert_text_to_image(r, fn.replace('.txt', '.png'))
                    self.send_image_weixin(self.weixin_robot_url, fn.replace('.txt', '.png'))

            # 非跳板机
            for x in hosts:
                if x['jump'] == None:
                    logger.debug('ssh {} {}@{}'.format(x['name'], x['username'], x['host']))
                    ssh.connect(hostname=x['host'],
                                port=x['port'],
                                username=x['username'],
                                key_filename=x['key'])

                    # stdin,stdout,stderr = ssh.exec_command('hostname; ps aux | grep python | grep -v grep');
                    # r = str(stdout.read(), encoding='utf-8')

                    s = ssh.invoke_shell()
                    s.send('hostname; ps aux | grep python | grep -v grep\r\n')
                    r = self._ssh_shell_recv(s)

                    # logger.debug(r)
                    fn = os.path.join(self.basedir, x['name']) + '.txt'
                    with open(fn, 'w') as f:
                        f.write(r)
                    logger.debug("{} get_payload done".format(x['name']))
                    self.convert_text_to_image(r, fn.replace('.txt', '.png'))
                    self.send_image_weixin(self.weixin_robot_url, fn.replace('.txt', '.png'))

        except Exception as e:
            logger.error(e)
            raise(e)

    def _send_weixin(self, url, data):
        headers = {'Content-Type': 'application/json'}
        try:
            if data['msgtype'] != 'image':
                logger.debug('send to {}:\n{}'.format(url, json.dumps(data, indent=True)))
            else:
                logger.debug('send image to {}'.format(url))
            if self.debug:
                result = {'resulte': 'fake result'}
            else:
                result = requests.post(url, headers=headers, json=data).text
            logger.debug('recv {}:\n{}'.format(url, json.dumps(result, indent=True)))
            return result
        except Exception as e:
            logger.error(e)
            raise(e)

    def send_text_weixin(self, url, message):
        strlen = len(message)
        begin = 0
        end = strlen
        mss = 4096
        while strlen > begin:
            if strlen > begin + mss:
                end = begin + mss
            else:
                end = strlen
            data = {
                'msgtype': 'text',
                'text': {
                    'content': message[begin:end],
                    'mentioned_list': ["@all"],
                }
            }
            self._send_weixin(url, data)
            begin = end

    def send_markdown_weixin(self, url, message):
        tm = time.localtime()
        msg = '{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d} 周{}'.format(
            tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min,
            tm.tm_sec, weekday[tm.tm_wday])

        data = {
            'msgtype': 'markdown',
            'markdown': {
                'content': '<font color="comment">AI状态检查日报</font>\n<font color="warnning">{}</font>\n{}'.format(msg, message),
                'mentioned_list': ["李云腾"],
            }
        }
        self._send_weixin(url, data)

    def send_image_weixin(self, url, image_path):
        try:
            with open(image_path, 'rb') as f:
                data = f.read()
                encodestr = base64.b64encode(data)
                image_data = str(encodestr, 'utf-8')
                md = hashlib.md5()
                md.update(data)
                image_md5 = md.hexdigest()
        except Exception as e:
            raise(e)
        data = {
            'msgtype': 'image',
            'image': {
                'base64': image_data,
                'md5': image_md5,
            }
        }
        self._send_weixin(url, data)

    def send_file_weixin(self, url, file_path):
        try:
            data = {'media': open(file_path, 'rb')}
            r = requests.post(url=weixin_media_id_url, files=data)
        except Exception as e:
            logger.debug(r.json())
            raise(e)
        data = {
            'msgtype': 'file',
            'file': {
                'media_id': r.json()['media_id']
            }
        }
        self._send_weixin(url, data)

    def convert_text_to_image(self, text, filename):
        width = 1920
        height = 1080
        n = len(text.split('\r\n'))
        height = (n * 24)
        text = text.replace('\r\n', '\n')

        im = Image.new("RGB", (width, height), (0, 0, 0))
        dr = ImageDraw.Draw(im)
        # font = ImageFont.truetype(os.path.join('fonts','msyh.ttf'), 20)
        font = ImageFont.truetype(os.path.join('fonts','DejaVuSansMono.ttf'), 20)
        dr.text((50, 50), text, font=font, fill='#ffffff')
        im.save(filename)
        logger.debug('convert {}x{}({}) image {}'.format(width, height, n, filename))

    def run(self):
        tm = time.localtime()
        if tm.tm_hour in range(6,9):
            n = '早上'
        elif tm.tm_hour in range(9,12):
            n = '上午'
        elif tm.tm_hour in range(12,14):
            n = '中午'
        elif tm.tm_hour in range(14,19):
            n = '下午'
        else:
            n = '晚上'
        msg = '{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d} 周{} {} 打卡'.format(
            tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min,
            tm.tm_sec, n, weekday[tm.tm_wday])

        self.send_text_weixin(self.weixin_robot_url, msg)
        self.capture_images()
        self.get_payload()


def run(basedir, debug=False):
    x = OnCall(basedir, debug)
    x.run()
