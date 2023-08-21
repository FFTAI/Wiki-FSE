import fi_fse
import time

server_ip_list = []


def main():
    server_ip_list = fi_fse.broadcast_func_with_filter(filter_type="AbsEncoder")

    if server_ip_list:

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            fi_fse.get_config(server_ip_list[i])

        print('\n')
        time.sleep(1)

        # set the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            dict = {
                'home_offset': 0,
            }
            fi_fse.set_config(server_ip_list[i], dict)

        print('\n')
        time.sleep(1)

        # get the communication configuration of all FAS
        for i in range(len(server_ip_list)):
            fi_fse.get_config(server_ip_list[i])

        print('\n')

        # reboot all FAS
        for i in range(len(server_ip_list)):
            fi_fse.reboot(server_ip_list[i])


if __name__ == '__main__':
    main()
