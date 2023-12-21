/**
 * @file demo_get_measured.cpp
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
    // while (1)
    // {
        for (int i = 0; i < ser_num; i++)
        {
            std::printf("IP: %s sendto get measured fse ---> ", ser_list[i].c_str());
            fse->demo_get_measured(ser_list[i], NULL, ser_msg);
            std::printf("%s\n", ser_msg);

            rapidjson::Document msg_json;
            if (msg_json.Parse(ser_msg).HasParseError())
            {
                logger->fi_logger_error("fi_decode() failed");
                return 0;
            }
            std::printf("angle: %.9f, radian: %.9f\n", msg_json["angle"].GetDouble(), msg_json["radian"].GetDouble());
        }
    //     usleep(500);
    // }

    return 0;
}
