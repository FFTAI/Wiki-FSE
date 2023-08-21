abs Encoder 测试和配置python3脚本

abs_angle.py   测试绝编实时角度值
abs_dev_info.py  获取绝编设备信息
abs_get_config.py  获取绝编网络配置信息
abs_reboot.py      重启绝编
abs_set_config_ip.py  设置绝编网络配置信息



配置abs 静态ip：
1. 打开 abs_set_config_ip.py 文件
2. 修改49行，set_config_dict中的配置选项，如下,只需要修改 staticIP 和 gateway 即可，并且 staticIP 和 gateway前三个数字一致
   set_config_dict = {
                        'DHCP_enable':False,
                        'staticIP':'10.10.10.123',  
                        'gateway': '10.10.10.1',
                        'subnet':'255.255.255.0',
                        'primaryDNS':'',
                        'secondaryDNS':'',
                      }
3. 运行python3 abs_set_config_ip.py即可完成配置。

4. 配置完成后，可通过 运行python3 abs_angle.py 测试设备IP地址和获取到的绝遍角度