#include "../include/fi_main.h"

FSE *fse = new FSE();
Logger *logger = new Logger();

int main()
{
    char *comm_config_set = "{\"method\":\"SET\", \
        \"reqTarget\":\"/config\", \
        \"property\":\"\", \
        \"home_offset\":5}";

    char ser_msg[1024] = {0};
    fse->demo_broadcase_filter(ABSCODER);
    if (fse->server_ip_filter_num == 0)
    {
        logger->fi_logger_error("Cannot find server");
        return 0;
    }

    for (int i = 0; i < fse->server_ip_filter_num; i++)
    {
        std::printf("IP: %s sendto reboot fse ---> ", fse->server_ip_filter[i].c_str());

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_ctrl_config_get(fse->server_ip_filter[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);
        usleep(10);

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_ctrl_config_set(fse->server_ip_filter[i], comm_config_set, ser_msg);
        std::printf("%s\n", ser_msg);
        sleep(3);

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_ctrl_config_get(fse->server_ip_filter[i], NULL, ser_msg);
        std::printf("%s\n", ser_msg);
        sleep(1);

        memset(ser_msg, 0, sizeof(ser_msg));
        fse->demo_reboot_fse(fse->server_ip_filter[i], NULL, ser_msg);
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
