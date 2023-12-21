/**
 * @file demo_comm_config_set.cpp
 * @author Afer
 * @brief
 * @version 0.1
 * @date 2023-12-21
 * @note pass-test
 *
 * @copyright Copyright (c) 2023
 *
 */
#include "../include/fi_main.h"

FSE *fse = new FSE();
Logger *logger = new Logger();

int main()
{
    char *comm_config_set = "{\"method\":\"SET\", \
        \"reqTarget\":\"/config\", \
        \"property\":\"\", \
        \"name\":\"FSE\", \
        \"DHCP_enable\":false, \
        \"SSID\":\"fftai-12\", \
        \"password\":\"fftai2015\", \
        \"static_IP\":[192,168,137,204], \
        \"gateway\":[192,168,137,1], \
        \"subnet_mask\":[255,255,255,0], \
        \"dns_1\":[114,114,114,114], \
        \"dns_2\":[8,8,8,8]}";

    char ser_msg[1024] = {0};
    fse->demo_broadcase_filter(ABSCODER);
    if (fse->server_ip_filter_num == 0)
    {
        logger->fi_logger_error("Cannot find server");
        return 0;
    }

    std::string ser_list[254] = {""};
    memset(ser_list, 0, sizeof(ser_list));
    memcpy(ser_list, fse->server_ip_filter, sizeof(ser_list));
    int ser_num = fse->server_ip_filter_num;

    for (int i = 0; i < ser_num; i++)
    {
        std::printf("IP: %s sendto set_comm_config ---> ", ser_list[i].c_str());
        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_comm_config_set(ser_list[i], comm_config_set, ser_msg);
        std::printf("%s\n", ser_msg);

        rapidjson::Document msg_json;
        if (msg_json.Parse(ser_msg).HasParseError())
        {
            logger->fi_logger_error("fi_decode() failed");
            return 0;
        }
        std::cout << "status: " << msg_json["status"].GetString() << std::endl;
        usleep(100);

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_reboot_fse(ser_list[i], NULL, ser_msg);
        sleep(6);

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_comm_config_get(ser_list[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);
    }

    return 0;
}
