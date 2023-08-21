import fi_fse


def main():
    server_ip_list = fi_fse.broadcast_func()
    comm_root_list = []
    comm_root = ""

    if server_ip_list:
        for i in range(len(server_ip_list)):
            comm_root = fi_fse.get_comm_root(server_ip_list[i])
            comm_root_list.append(comm_root)

    print("The communication root is: ", comm_root)


if __name__ == '__main__':
    main()
