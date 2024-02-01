import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()

from fkey.models import Router, Interface, Area, OSPFNetwork, OSPFProcess


# 设备接口信息
csr1_ifs = [{'ifname': "GigabitEthernet1", 'ip': "137.78.5.254", 'mask': "255.255.255.0"},
            {'ifname': "GigabitEthernet2", 'ip': "61.128.1.254", 'mask': "255.255.255.0"},
            {'ifname': "Loopback0", 'ip': "1.1.1.1", 'mask': "255.255.255.255"}]

csr2_ifs = [{'ifname': "GigabitEthernet1", 'ip': "61.128.1.1", 'mask': "255.255.255.0"},
            {'ifname': "GigabitEthernet2", 'ip': "202.100.1.1", 'mask': "255.255.255.0"},
            {'ifname': "Loopback0", 'ip': "2.2.2.2", 'mask': "255.255.255.255"}]

# 设备OSPF信息
csr1_ospf = {"process_id": 1,
             "router_id": "1.1.1.1",
             "areas": [{'area_id': 0, 'networks': [{'ip': "137.78.5.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "61.128.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "1.1.1.1", 'wildmask': "0.0.0.0"}]}]}

csr2_ospf = {"process_id": 1,
             "router_id": "2.2.2.2",
             "areas": [{'area_id': 0, 'networks': [{'ip': "61.128.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "202.100.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "2.2.2.2", 'wildmask': "0.0.0.0"}]}]}

all_network_data = [{'ip': "10.1.1.201", 'routername': 'CSR1', 'interfaces': csr1_ifs, 'ospf': csr1_ospf},
                    {'ip': "10.1.1.202", 'routername': 'CSR2', 'interfaces': csr2_ifs, 'ospf': csr2_ospf}]


# 删除所有的条目

for csr in Router.objects.all():
    csr.interface.all().delete()
    for area in csr.ospfprocess.area.all():
        area.ospfnetwork.all().delete()
        area.delete()
    csr.ospfprocess.delete()
    csr.delete()

for device in all_network_data:
    router_device = Router(routername=device['routername'], ip=device['ip'])
    router_device.save()

    for ifs in device['interfaces']:
        new_if = Interface(router=router_device, interface_name=ifs['ifname'], interface_ip=ifs['ip'], mask=ifs['mask'])
        new_if.save()

    router_device_process = OSPFProcess(router=router_device,
                                        processid=device["ospf"]["process_id"],
                                        routerid=device["ospf"]["router_id"])
    router_device_process.save()

    for device_area in device["ospf"]["areas"]:
        router_device_area = Area(ospfprocess=router_device_process, area_id=device_area["area_id"])
        router_device_area.save()
        for net in device_area["networks"]:
            new_net = OSPFNetwork(area=router_device_area, network=net['ip'], wildmask=net['wildmask'])
            new_net.save()
