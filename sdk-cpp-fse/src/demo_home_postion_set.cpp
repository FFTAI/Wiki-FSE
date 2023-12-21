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
    for (int i = 0; i < ser_num; i++)
    {
        std::printf("IP: %s sendto set position fse ---> ", ser_list[i].c_str());
        fse->demo_home_position_set(ser_list[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);

        rapidjson::Document msg_json;
        if (msg_json.Parse(ser_msg).HasParseError())
        {
            logger->fi_logger_error("string turn to json failed");
            return 0;
        }
        std::cout << "status: " << msg_json["status"].GetString() << std::endl;
    }

    return 0;
}
