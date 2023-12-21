/**
 * @file demo_lookup.cpp
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
    fse->demo_broadcase();
    for (int i = 0; i < fse->server_ip_num; i++)
    {
        std::cout << fse->server_ip[i] << std::endl;
    }
    return 0;
}
