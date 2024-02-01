#!/usr/bin/env python3
# -*- coding=utf-8 -*-
# 本脚由亁颐堂现任明教教主编写，用于乾颐盾Python课程！
# 教主QQ:605658506
# 亁颐堂官网www.qytang.com
# 教主技术进化论拓展你的技术新边疆
# https://ke.qq.com/course/271956?tuin=24199d8a
from ncclient import manager
from ncclient.operations import RPCError
import lxml.etree as ET


def csr_netconf_config(ip, username, password, payload_xml, port='830'):
    # 使用NETCONF客户端ncclient,连接网络设备
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            # 发送构建的XML数据,到网络设备,修改配置(edit_cofig)
            response = m.edit_config(target='running', config=payload_xml).xml
            # 从字符串数据转换到XML
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # 从XML数据,转换到字符串,并返回
        return ET.tostring(data).decode()


def csr_netconf_monitor(ip, username, password, payload_xml, port='830'):
    # 使用NETCONF客户端ncclient,连接网络设备
    with manager.connect(host=ip,
                         port=port,
                         username=username,
                         password=password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        try:
            # 发送构建的XML数据,到网络设备,修改配置(edit_cofig)
            response = m.get(payload_xml).xml
            # 从字符串数据转换到XML
            data = ET.fromstring(response.encode())
        except RPCError as e:
            data = e._raw

        # 从XML数据,转换到字符串,并返回
        return ET.tostring(data).decode()


if __name__ == '__main__':
    pass
