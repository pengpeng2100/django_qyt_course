import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()
from fkey.models import Router
from datetime import datetime, timedelta

# 正则表达式
for router in Router.objects.filter(routername__regex=r'^[Cc][Ss][Rr]\d$'):
    print(router)


# 多表查询,类似于联合查询, 使用get或者filter都可以
router_join_filter = Router.objects.get(routername__regex=r'^[Cc][Ss][Rr]\d$',
                                        interface__interface_name='GigabitEthernet1',
                                        interface__interface_ip__contains='254',
                                        ospfprocess__processid=1)
print(router_join_filter)

# 对特定路由器的接口进行过滤,然后对满足条件的接口进行迭代
for interface in router_join_filter.interface.filter(interface_name__startswith='GigabitEthernet'):
    print(interface.interface_name)
    print(interface.interface_ip)
    print(interface.router.ospfprocess.routerid)

# one to one 直接得到路由器的ospf_process
print(router_join_filter.ospfprocess.processid)

# 打印路由器下所有区域下的所有网络
for area in router_join_filter.ospfprocess.area.all():
    for network in area.ospfnetwork.all():
        print(network)

# 时间过滤
for cpu_usage in router_join_filter.cpuusage.filter(cpu_useage_datetime__gte=datetime.now() - timedelta(hours=3)):
    print(cpu_usage.cpu_useage_datetime)
    print(cpu_usage.cpu_useage_percent)
