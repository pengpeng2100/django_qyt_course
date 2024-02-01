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

from fkey.netconf_module.netconf_monitor import csr_monitor_cpu
import datetime
import time
from fkey.models import Router, CPUUsage

username = 'admin'
password = 'Cisc0123'


def get_info_writedb(ip, seconds):
    CPUUsage.objects.all().delete()
    while seconds > 0:
        # cpmCPUTotal5sec
        cpu_info = csr_monitor_cpu(ip, username, password)

        # 把数据写入数据库
        router1 = Router.objects.get(ip=ip)
        print(router1)
        cpu_usage_1 = CPUUsage(router=router1, cpu_useage_percent=cpu_info)
        cpu_usage_1.save()

        # 每五秒采集一次数据
        time.sleep(5)
        seconds -= 5


def cpu_read_db(device_ip, last_seconds=0):
    router1 = Router.objects.get(ip=device_ip)

    # 提取时间与CPU利用率信息
    if last_seconds:
        now = datetime.datetime.now()
        before_last_seconds = now - datetime.timedelta(seconds=last_seconds)
        cpu_result = CPUUsage.objects.filter(router=router1, cpu_useage_datetime__gte=before_last_seconds)
    else:
        cpu_result = CPUUsage.objects.filter(router=router1)

    time_list = [i.cpu_useage_datetime.strftime('%H:%M:%S') for i in cpu_result]
    cpu_list = [i.cpu_useage_percent for i in cpu_result]

    return time_list, cpu_list


if __name__ == '__main__':
    get_info_writedb('10.1.1.201', 30)
    print(cpu_read_db('10.1.1.201', 60))
