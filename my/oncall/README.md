# 检查AI资源，并截图发送到企业微信

### 功能
  * 截取[grafana](http://grafana.addx.live)上AI相关图片,发送至企业微信robot.
  * 获取不同主机上AI程序信息，转成图片，发送至企业微信robot. 目前的主机：
     - 10.160.2.27  (欧洲）    跳板机: 52.80.136.41
     - 10.160.1.73  (欧洲)     跳板机: 52.80.136.41
     - 10.100.2.89  (美国）     跳板机: 52.80.136.41
     - 10.100.2.153 (美国)     跳板机: 52.80.136.41
     - 52.81.37.85  (中国)

### 文件
  * main.py             - python 程序
  * id_rsa              - 跳板机，中国节点使用的ssh key
  * fonts               - 将文本转换成图片使用的字体

### 依赖
  1. *python3* *pip3*

  2. *selenium* 用来自动控制浏览器 `pip3 install selenium`

      * *Chrome*浏览器 需要chromedriver-binary

          `pip3 install chromedriver-binary`


      * *Firefox*浏览器 不支持

      * 其他  不支持


  3. *paramiko* 支持ssh
     `pip3 install paramiko`

  4. *pillow* 将文本转换为图片
     `pip3 install pillow`


### 运行
  * 直接运行
     `python3 main.py`

  * *debug* 模式,不会向企业微信发送消息
    `python3 main.py -d`

  * 定时启动
    1. 配置crontab `crontab -e`

    2. 每天8:00 22:00 自动运行
       ```
        0 8,22 * * * cd /Users/addx/work/oncall && /usr/local/bin/python3 /Users/addx/work/oncall/oncall.py
        ```
    3. 检查配置 `crontab -l`
