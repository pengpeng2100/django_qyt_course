#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
import re
from jinja2 import Template
tem_path = './jinja2_template/'


def netconf_if_ip(interface, address, mask):
    interface_name, interface_no = re.match('([a-zA-Z]*)([0-9].*)', interface).groups()
    with open(tem_path + 'interface_ip.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(if_type=interface_name, if_no=interface_no, ip_address=address, net_mask=mask)
    return netconf_payload


def netconf_if_no_shutdown(interface):
    with open(tem_path + 'interface_no_shutdown.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(interface_name=interface, interface_status='true')
    return netconf_payload


def netconf_ospf_router_id(process_id, router_id):
    with open(tem_path + 'ospf_router_id.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(process_id=process_id, router_id=router_id)
    return netconf_payload


def netconf_ospf_network(process_id, ip, mask, area):
    with open(tem_path + 'ospf_network.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(process_id=process_id, network=ip, wild_mask=mask, area=area)
    return netconf_payload


def netconf_monitor_cpu(monitor_type):
    with open(tem_path + 'monitor_cpu.xml') as f:
        netconf_template = Template(f.read())
    netconf_payload = netconf_template.render(monitor_type_use=monitor_type)
    return netconf_payload


if __name__ == '__main__':
    print(netconf_if_ip('GigabitEthernet2', '61.128.1.1', '255.255.255.0'))
    print(type(netconf_if_ip('GigabitEthernet2', '61.128.1.1', '255.255.255.0')))