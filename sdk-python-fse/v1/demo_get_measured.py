import fi_fse
import time

Server_IP_list = []


def main():
    Server_IP_list = fi_fse.broadcast_func_with_filter(filter_type="AbsEncoder")

    print(Server_IP_list)
    if len(Server_IP_list) == 0:
        print('there is no abs')
        return

    while True:
        angle, radian = fi_fse.get_measured(Server_IP_list)
        print("angle: ", angle, "radian: ", radian)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
