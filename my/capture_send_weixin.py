#!/usr/bin/env python3

# -*- coding: utf-8 -*-

# a.py - a

# Date   : 2020/12/09
import requests
import base64
import hashlib
import json
import os
import time

# pip3 install chromedriver-binary-auto selenium paramiko
try:
    import paramiko
    import chromedriver_binary
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
except Exception as e:
    print('pip3 install chromedriver-binary-auto selenium paramiko')
    raise(e)

username = 'yshi@addx.ai'
password = '19910310lang+'
loginurl = 'http://grafana.addx.live/login'
url = 'http://grafana.addx.live/d/UWulzimMk/hou-duan?orgId=1&from=now-2d&to=now'
weixin_robot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f3ee8839-f66c-4470-a36d-465b7562b306"
weixin_media_id_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=f3ee8839-f66c-4470-a36d-465b7562b306&type=file"

def capture_images(basedir):
    chrome_options = Options().add_argument('headless')
    brower = webdriver.Chrome(chrome_options=chrome_options)

    try:
        brower.get(loginurl)

        brower.find_element_by_name('user').clear()
        brower.find_element_by_name('user').send_keys(username)
        brower.find_element_by_name('password').clear()
        brower.find_element_by_name('password').send_keys(password)
        brower.find_element_by_class_name('login-button-group').find_element_by_tag_name('button').click()


        brower.maximize_window()

        brower.get(url)
        time.sleep(3)
        x = brower.find_element_by_id('panel-79')
        brower.execute_script('arguments[0].scrollIntoView();', x)
        time.sleep(5)
        brower.save_screenshot(os.path.join(basedir, 'backend.png'))


        brower.get('http://grafana.addx.live/d/9CWBz0bi3/ou-zhou-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-eu-gpu-node2')
        time.sleep(8)
        brower.save_screenshot(os.path.join(basedir, 'ou-node2.png'))

        brower.get('http://grafana.addx.live/d/9CWBz0bil/mei-guo-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-us-gpu-node4')
        time.sleep(8)
        brower.save_screenshot(os.path.join(basedir, 'us-node4.png'))

        brower.get('http://grafana.addx.live/d/9CWBz0bil/mei-guo-jie-dian-zhu-ji-jian-kong?orgId=1&var-job=prod-us-gpu-node5')
        time.sleep(8)
        brower.save_screenshot(os.path.join(basedir,'us-node5.png'))

        brower.close()
        brower.quit()

    except Exception as e:
        brower.quit()
        raise(e)

def get_load():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 跳板机
    ssh.connect(hostname='52.80.136.41',
                port=32222,
                username='ec2-user',
                key_filename='/Users/lyt/.ssh/id_rsa')
    s = ssh.invoke_shell()
    s.send('sudo su -\n')
    s.send('hostname\n')
    buf = ''
    while True:
        r = s.recv(9999)
        r = str(r, encoding='utf-8')
        if r.endswith('# '):
            break

    result = {}
    hosts = [
        {'username': 'ubuntu', 'port': 32222, 'host':'10.100.2.89', 'name': '美国-1'},
        {'username': 'ubuntu', 'port': 32222, 'host':'10.100.2.153', 'name': '美国-2'},
        {'username': 'ubuntu', 'port': 32222, 'host':'10.160.1.73', 'name': '欧洲-1'}
    ]

    for x in hosts:
        s.send('ssh -p{} {}@{} "ps aux | grep python | grep -v grep"\r\n'.format(
            x['port'], x['username'], x['host']))
        buf = ''
        while True:
            r = s.recv(99999)
            r = str(r, encoding='utf-8')
            buf += r
            if r.endswith('# '):
                break
        result[x['name']] = buf

    return result

def send_weixin(data):
    headers = {'Content-Type': 'application/json'}
    try:
        result = requests.post(weixin_robot_url, headers=headers, json=data)
        print(result.text)
    except Exception as e:
        raise(e)

def send_message_weixin(message):
    data = {
        'msgtype': 'text',
        'text': {
            'content': message
        }
    }
    send_weixin(data)

def send_image_weixin(image_path):
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
    send_weixin(data)

def send_file_weixin(file_path):
    try:
        data = {'media': open(file_path, 'rb')}
        r = requests.post(url=weixin_media_id_url, files=data)
    except Exception as e:
        print(r.json())
        raise(e)

    data = {
        'msgtype': 'file',
        'file': {
            'media_id': r.json()['media_id']
        }
    }
    send_weixin(data)

if __name__ == '__main__':
    tm = time.localtime(time.time())
    basedir = os.path.join('.', '{:04d}_{:02d}_{:02d}_{:02d}_{:02d}_{:02d}'.format(
        tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec))

    if not os.path.exists(basedir):
        os.mkdir(basedir)

    # 截图
    capture_images(basedir)

    msg = '{:04d}/{:02d}/{:02d} {:02d}:{:02d}:{:02d} 周{} 打卡'.format(
        tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min,
        tm.tm_sec, tm.tm_wday + 1)

    # 微信发送图片
    send_message_weixin(msg)
    for x in ['./backend.png', './ou-node2.png', './us-node4.png', './us-node5.png']:
        send_image_weixin(os.path.join(basedir, x))

    # ssh 获取 load
    msg = get_load();
    for x in msg:
        # 保存文件
        with open(os.path.join(basedir, x+'.txt'), 'w') as f:
            f.write(msg[x])

        send_file_weixin(os.path.join(basedir, x+'.txt'))

        # strlen = len(msg[x])
        # begin = 0
        # end = strlen
        # while strlen > begin:
        #     if begin + 5100 > strlen:
        #         end = strlen
        #     else:
        #         end = begin + 5100
        #     print(msg[x][begin:end])
        #     send_message_weixin(msg[x][begin:end])
        #     begin += 5100
