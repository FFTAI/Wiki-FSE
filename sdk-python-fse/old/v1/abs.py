#!/usr/bin/env Python
# -*- coding:UTF-8 -*-
# author：作者    date:2020/1/8 time:21:45
# 代码自动补齐----------------------------
# p: parameter 参数
# m: method 方法
# f: function 函数
# v: variable 变量
# c: class 类
# 快捷键---------------------------------
# 复制上一行：crtl + D# 删除这一行：crtl + Y
# 增加/删除注释：Ctrl + /
# 折叠代码：crtl + -       全部：crtl + shift + -
# 展开代码：crtl + +       全部：Ctrl + shift + +
# 回车换行：shift + Enter# 查找：Ctrl + F
# 替换：Ctrl + R# 自动排版：Ctrl + Alt + L
# 缩进：Tab# 反缩进：Shift + Tab# 找寻变量\函数\参数定义的位置：Ctrl + 鼠标单击
# 逐步选定相邻的代码：Ctrl + W
# 同时选定多行并且编辑：Alt + 鼠标左击，退出：Esc
# 变成指定代码块：Ctrl + Alt + T

import socket
import time
import json
from ctypes import CDLL
import json
import socket

udp_sorket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_sorket.settimeout(2)
udp_sorket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# network = '192.168.30.255'
network = '192.168.31.255'

remote_port = 2334

DeviceModel = 'ABS_Encoder'


def get_ip(ip):
    try:
        udp_sorket.connect(('10.255.255.255', 1))
        ip = udp_sorket.getsockname()[0]
    except Exception:
        return False
    return True


# 广播获取设备信息，ip地址等
def brosdcast_func():
    data = {
        "id": 0,
        "method": "Device.Info",
        "params": "",
    }

    json_str = json.dumps(data)
    print(json_str)
    found_abs = False
    address_list = []

    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (network, remote_port))  # udp 广播
        print('send broadcast')
        while True:
            try:
                r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
                # print('udp received from {}:{}'.format(addr, r_data.decode('utf-8')))
                if address_list.count(addr[0]) == 0:  # 如果列表中没有此值，则添加上
                    device_json_obj = json.loads(r_data.decode('utf-8'))
                    if device_json_obj.get('result').get('dev_model') == DeviceModel:  # 查看设备回复的设备类型是否是abs
                        address_list.append(addr[0])  # 加入到列表中

                found_abs = True
            except socket.timeout:
                if found_abs:
                    break;
                else:
                    print('do not receive any abs')
                    break
    return address_list


# 广播获取设备信息，ip地址等
def get_dev_info(ip):
    data = {
        "id": 0,
        "method": "Device.Info",
        "params": "",
    }

    json_str = json.dumps(data)

    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('devive info {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')


# 获取每个设备的 abs角度
# addrList  设备ip地址列表
# angle_dirt abs 角度字典 ： {ip : angle}
def get_angle(addrList, angle_dirt):
    data = {
        "id": 0,
        "method": "Encoder.Angle",
        "params": "",
    }
    json_str = json.dumps(data)
    for i in addrList:
        udp_sorket.sendto(json_str.encode('utf-8'), (i, remote_port))  # 发送获取设备abs角度的指令
        try:
            r_data, addr = udp_sorket.recvfrom(1024)
            # print('udp received from {}:{}'.format(addr, r_data.decode('utf-8')))
            json_obj = json.loads(r_data.decode('utf-8'))  # 解析json数据包
            d_abs = [json_obj.get('result').get('angle'), json_obj.get('result').get('radian')]  # 获取abs角度值 ，弧度值
            # print(d_abs)
            angle_dirt[i] = d_abs  # 将abs值放入到 键为IP地址的 字典中
            # print(abs_angle_dirt)
        except socket.timeout:
            print('get angle timeout:', i, end='\r\n')
            print('')
            print('')


# 获取每个设备的 rssi
# addrList  设备ip地址列表
# rssi_dirt 设备rssi值字典 ： {ip : rssi}
def get_rssi(addrList, rssi_dirt):
    data = {
        "id": 0,
        "method": "Device.Info",
        "params": "",
    }
    json_str = json.dumps(data)
    for i in addrList:
        udp_sorket.sendto(json_str.encode('utf-8'), (i, remote_port))  # 发送获取设备abs角度的指令
        try:
            r_data, addr = udp_sorket.recvfrom(1024)
            # print('udp received from {}:{}'.format(addr, r_data.decode('utf-8')))
            json_obj = json.loads(r_data.decode('utf-8'))  # 解析json数据包
            if json_obj.get('result').get('connect_mode') == 'wifi':
                d_rssi = json_obj.get('result').get('RSSI')  # 获取abs角度值 ，弧度值
            else:
                d_rssi = 'eth'
            # print(d_abs)
            rssi_dirt[i] = d_rssi  # 将abs值放入到 键为IP地址的 字典中
            # print(abs_angle_dirt)
        except socket.timeout:
            print('get angle timeout:', i, end='\r\n')
            print('')
            print('')

        #  重启指令


def reboot(addrList):
    data = {
        "id": 0,
        "method": "reboot",
        "params": "",
    }
    json_str = json.dumps(data)
    for i in addrList:
        udp_sorket.sendto(json_str.encode('utf-8'), (i, remote_port))  # 发送reboot指令
        try:
            r_data, addr = udp_sorket.recvfrom(1024)
            print('udp received from {}:{}'.format(addr, r_data.decode('utf-8')))
        except socket.timeout:
            print('timeout,send agin:', i)
            udp_sorket.sendto(json_str.encode('utf-8'), (i, remote_port))  # 发送reboot指令


def reboot(_ip):
    data = {
        "id": 0,
        "method": "reboot",
        "params": "",
    }
    json_str = json.dumps(data)
    udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # 发送reboot指令
    try:
        r_data, addr = udp_sorket.recvfrom(1024)
        print('udp received from {}:{}'.format(addr, r_data.decode('utf-8')))
    except socket.timeout:
        print('timeout,send agin:', _ip)
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # 发送reboot指令


def config_dev_name(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入dev_name:')
    data['params'] = {'dev_name': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_SSID(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入SSID:')
    data['params'] = {'SSID': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_password(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入password:')
    data['params'] = {'password': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_hostname(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入hostname:')
    data['params'] = {'hostname': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_DHCP_enable(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入\'true\' or \'false\':')
    while not (str == 'true' or str == 'false'):
        str = input('请输入\'true\' or \'false\':')
    if (str == 'true'):
        data['params'] = {'DHCP_enable': True}
    else:
        data['params'] = {'DHCP_enable': False}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_staticIP(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入staticIP:')
    data['params'] = {'staticIP': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_subnet(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入subnet:')
    data['params'] = {'subnet': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_primaryDNS(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入primaryDNS:')
    data['params'] = {'primaryDNS': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


def config_secondaryDNS(_ip):
    data = {
        "id": 0,
        "method": "Set.Config",
        "params": "",
    }

    print(data)
    str = input('请输入secondaryDNS:')
    data['params'] = {'secondaryDNS': str}
    json_str = json.dumps(data)
    for i in range(3):  # Wi-Fi 连接时，广播一次不一定能全部接收到所有设备的回复 ，需要多广播几次
        udp_sorket.sendto(json_str.encode('utf-8'), (_ip, remote_port))  # udp 广播
        try:
            r_data, addr = udp_sorket.recvfrom(1024)  # 接收局域网中回复数据，每次接收最大1024
            print('result {}:{}'.format(addr, r_data.decode('utf-8')))
            break
        except socket.timeout:
            print('socke timeout')
    reboot(_ip)


# set_config_dict_process = {'1':config_dev_name,
#                            '2':config_SSID,
#                            '3':config_password,
#                                 '4':config_hostname,
#                                 '5':config_DHCP_enable,
#                                 '6':config_staticIP,
#                                 '7':config_subnet,
#                                 '8':config_primaryDNS,
#                                 '9':config_secondaryDNS,
#                                 }

#  重启指令
def set_config(_ip):
    set_config_dict = {'1': 'dev_name',
                       '2': 'SSID',
                       '3': 'password',
                       '4': 'hostname',
                       '5': 'DHCP_enable',
                       '6': 'staticIP',
                       '7': 'subnet',
                       '8': 'primaryDNS',
                       '9': 'secondaryDNS',
                       }

    print(set_config_dict)
    num = input('请输入需要配置的选项的序号：')
    while set_config_dict.get(num) == None:
        num = input('该配置选项不存在，请重新输入需要配置的选项的序号：')
    print('需要配置的选项为：', set_config_dict.get(num))
    # set_config_dict_process.get(num)()
    if num == '1':
        config_dev_name(_ip)
    elif num == '2':
        config_SSID(_ip)
    elif num == '3':
        config_password(_ip)
    elif num == '4':
        config_hostname(_ip)
    elif num == '5':
        config_DHCP_enable(_ip)
    elif num == '6':
        config_staticIP(_ip)
    elif num == '7':
        config_subnet(_ip)
    elif num == '8':
        config_primaryDNS(_ip)
    elif num == '9':
        config_secondaryDNS(_ip)
