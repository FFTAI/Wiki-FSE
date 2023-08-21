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

Server_IP_list = []
abs_angle_dirt = {}


def main():
    Server_IP_list = abs.brosdcast_func()  # 广播查询局域网下的所有abs
    print(Server_IP_list)
    abs.reboot(Server_IP_list)


if __name__ == '__main__':
    main()
