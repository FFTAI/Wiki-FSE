import numpy

import fi_fse
import time

server_ip_list = []


def main():
    server_ip_list = fi_fse.broadcast_func_with_filter(filter_type="AbsEncoder")

    if server_ip_list:

        for i in range(len(server_ip_list)):
            fi_fse.get_home_offset(server_ip_list[i])

        print('\n')


if __name__ == '__main__':
    main()
