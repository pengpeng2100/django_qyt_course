#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from fkey.netconf_module.yang_xml_maker_template import netconf_monitor_cpu
from fkey.netconf_module.netconf_request import csr_netconf_monitor
import xmltodict


def csr_monitor_cpu(device_ip, username, password, monitor_type='5s'):
    monitor_type_use = 'five-seconds'
    if monitor_type == '1m':
        monitor_type_use = 'one-minute'
    elif monitor_type == '5m':
        monitor_type_use = 'five-minutes'
    else:
        monitor_type_use = 'five-seconds'
    result_xml = csr_netconf_monitor(device_ip, username, password, netconf_monitor_cpu(monitor_type_use), port='830')
    xmldict = xmltodict.parse(result_xml)
    # pprint(xmldict)
    return xmldict['rpc-reply']['data']['cpu-usage']['cpu-utilization'][monitor_type_use]


if __name__ == '__main__':
    # 监控最近五秒钟CPU利用率
    print(csr_monitor_cpu('192.168.1.1', 'admin', 'Cisc0123', '5s'))