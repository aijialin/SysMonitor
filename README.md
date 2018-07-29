# SysMonitor

用python写的监控linux服务器各项性能的模块

## 支持
- [x] 实时检测CPU使用率
- [x] 实时检测内存使用率 
- [x] 实时检测带宽使用率
- [x] 实时检测IO使用率 
- [x] 获取CPU型号等信息

## 使用
**需要先安装iostat**
```python
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
``` 

## 输出
```python
{'cpu_usage': 2.0, 'io_usage': 0.0, 'mem_usage': 21.87150326134844, 'model_name': 'Intel(R) Xeon(R) CPU E5-26xx v3', 'net_usage': 0.0}
```