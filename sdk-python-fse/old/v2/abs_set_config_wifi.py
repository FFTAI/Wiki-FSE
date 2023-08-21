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

import abs
import time

Server_IP_list = ['192.168.31.71']
abs_angle_dirt = {}


def main():
    while True:
        # Server_IP_list = abs.brosdcast_func()  # 广播查询局域网下的所有abs

        # if len(Server_IP_list) == 0:
        #     print('there is no abs')
        #     break
        # print(Server_IP_list)
        # if len(Server_IP_list) > 1:
        #     ip_str = input('请输入需要修改的设备原IP:')
        # else:
        #     ip_str = Server_IP_list[0]
        # print(Server_IP_list.count(ip_str))
        # if Server_IP_list.count(ip_str) == 0:
        #     print('this ip is not in abs')
        #     continue
        ip_str = Server_IP_list[0]

        set_config_dict = {
            'DHCP_enable': False,
            'SSID': 'V3-4',
            'password': 'fo3.1415926',
            'staticIP': '192.168.31.55',
            'gateway': '192.168.31.1',
            'subnet': '255.255.255.0',
            'primaryDNS': '',
            'secondaryDNS': '',
        }
        print(set_config_dict)
        abs_config = set_config_dict.copy()  # 复制到abs_config

        for k, v in set_config_dict.items():
            if v == '':
                abs_config.pop(k)  # 如果某一键的值为空，则去除掉该配置
        print(abs_config)

        if 'DHCP_enable' in abs_config:
            if not (abs_config['DHCP_enable'] == True or abs_config['DHCP_enable'] == False):  # 判断DHCP_enable只能为True  或者 False
                print('err:set DHCP_enable err,please set True or False')
                return

        abs.set_config(ip_str, abs_config)
        abs.reboot(ip_str)

        return


if __name__ == '__main__':
    main()
