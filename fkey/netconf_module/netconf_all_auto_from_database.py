#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()

from fkey.netconf_module.yang_xml_maker_template import netconf_if_ip, netconf_if_no_shutdown
from fkey.netconf_module.yang_xml_maker_template import netconf_ospf_router_id, netconf_ospf_network
from fkey.netconf_module.netconf_request import csr_netconf_config
from fkey.models import Router

username = 'admin'
password = 'Cisc0123'


def netconf_all_auto():
    for csr in Router.objects.all():
        print('配置接口IP')
        print(csr)
        for interface in csr.interface.all():  # 迭代出每一个接口信息
            print(interface)
            # 配置IP地址
            csr_netconf_config(csr.ip, username, password, netconf_if_ip(interface.interface_name,
                                                                         interface.interface_ip,
                                                                         interface.mask))
            # no shutdown接口
            csr_netconf_config(csr.ip, username, password, netconf_if_no_shutdown(interface.interface_name))
        print('配置OSPF router-id')
        process = csr.ospfprocess
        print(process)
        csr_netconf_config(csr.ip, username, password, netconf_ospf_router_id(process.processid, process.routerid))
        print('宣告OSPF网络')
        for area in process.area.all():  # 迭代出每一个area
            print(area)
            for network in area.ospfnetwork.all():  # 迭代出每一个area的网络
                print(network)
                csr_netconf_config(csr.ip, username, password, netconf_ospf_network(process.processid, network.network, network.wildmask, area.area_id))


if __name__ == '__main__':
    netconf_all_auto()
