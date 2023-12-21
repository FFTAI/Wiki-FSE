/**
 * @file demo_reboot.cpp
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
    char ser_msg[1024] = {0};
    fse->demo_broadcase();
    if (fse->server_ip_num == 0)
    {
        logger->fi_logger_error("Cannot find server");
        return 0;
    }

    for (int i = 0; i < fse->server_ip_num; i++)
    {
        std::printf("IP: %s sendto reboot fse ---> ", fse->server_ip[i].c_str());
        fse->demo_reboot(fse->server_ip[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);

        rapidjson::Document msg_json;
        if (msg_json.Parse(ser_msg).HasParseError())
        {
            logger->fi_logger_error("fi_decode() failed");
            return 0;
        }
        std::cout << "status: " << msg_json["status"].GetString() << std::endl;
    }

    return 0;
}
