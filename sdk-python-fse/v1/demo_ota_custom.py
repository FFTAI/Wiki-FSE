import fi_fse
import time

server_ip_list = []


def main():
    server_ip_list = fi_fse.broadcast_func_with_filter(filter_type="AbsEncoder")
    version_str = '0.1.2.20'
    if server_ip_list:

        for i in range(len(server_ip_list)):
            fi_fse.ota_custom(server_ip_list[i], version_str)

        print('\n')
        time.sleep(1)


if __name__ == '__main__':
    main()