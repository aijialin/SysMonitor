#! /usr/bin/python3
# coding=utf8

from SysMonitor import monitor
import time, json

def get_info():
	info_dic = {
		"model_name"	:	monitor.get_cpu_info(category="model name"),
		"cpu_usage"		:	monitor.get_cpu_usage_info(), 
		"mem_usage"		:	monitor.get_mem_usage_info(),
		"net_usage"		:	monitor.get_net_usage_info(), 
		"io_usage"		:	monitor.get_io_usage_info(),
	}
	print(info_dic)

if __name__ == "__main__":
	for i in range(10):
		info = get_info()
		time.sleep(0.5)

