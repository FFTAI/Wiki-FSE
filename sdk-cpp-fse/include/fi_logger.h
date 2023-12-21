#ifndef __FI_LOGGER_H__
#define __FI_LOGGER_H__

#include <iostream>
#include <ctime>

class Logger
{
private:
    time_t rawtime = time(0);
    struct tm *timeinfo = localtime(&rawtime);
public:

private:
    void logger_parent(std::string msg);
    void logger_time_stamp();
public:
    Logger(/* args */);
    ~Logger();
    void fi_logger_info(std::string msg);
    void fi_logger_warning(std::string msg);
    void fi_logger_error(std::string msg);
};

Logger::Logger(/* args */)
{
    this->rawtime = time(0);
    this->timeinfo = localtime(&this->rawtime);
}

Logger::~Logger()
{
}


#endif // !__FI_LOGGER_H__
