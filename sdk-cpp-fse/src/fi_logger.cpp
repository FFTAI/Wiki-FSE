#include "../include/fi_logger.h"

void Logger::logger_parent(std::string msg)
{
    std::cout << msg << std::endl;
}

void Logger::logger_time_stamp()
{
    this->rawtime = time(0);
    this->timeinfo = localtime(&this->rawtime);
    std::cout << this->timeinfo->tm_hour << ":" << this->timeinfo->tm_min << ":" << this->timeinfo->tm_sec;
}

void Logger::fi_logger_info(std::string msg)
{
    this->logger_time_stamp();
    std::cout << "\e[1;32;40m[info]\e[0m";
    this->logger_parent(msg);   
}
void Logger::fi_logger_warning(std::string msg)
{
    this->logger_time_stamp();
    std::cout << "\e[1;33;40m[warning]\e[0m";
    this->logger_parent(msg);   
}
void Logger::fi_logger_error(std::string msg)
{
    this->logger_time_stamp();
    std::cout << "\e[1;31;40m[error]\e[0m";
    this->logger_parent(msg);   
}