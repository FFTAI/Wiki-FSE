/**
 * @file demo_ota_cloud.cpp
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

    for (int i = 0; i < fse->server_ip_filter_num; i++)
    {
        std::printf("IP: %s sendto ota cloud fse ---> ", fse->server_ip_filter[i].c_str());
        fse->demo_ota_cloud(fse->server_ip_filter[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);

        rapidjson::Document msg_json;
        if (msg_json.Parse(ser_msg).HasParseError())
        {
            logger->fi_logger_error("fi_decode() failed");
            return 0;
        }
        std::cout << "OTAstatus: " << msg_json["OTAstatus"].GetString() << std::endl;
    }

    return 0;
}
