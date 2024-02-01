from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, verbose_name='学员姓名')
    password = models.CharField(max_length=100, verbose_name='学员密码')
    # realname = models.CharField(max_length=100, verbose_name='真实姓名')
    email = models.EmailField(unique=True, verbose_name='邮箱')

    def __str__(self):
        return f"{self.__class__.__name__}( 学员姓名: {self.username} | 邮件: {self.email} )"


class Router(models.Model):
    routername = models.CharField(max_length=100, unique=True, verbose_name='路由器名称')
    ip = models.GenericIPAddressField(unique=True, verbose_name='IP地址')

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.routername} | IP: {self.ip} )"


class Interface(models.Model):
    router = models.ForeignKey(Router, related_name='interface', on_delete='CASCADE')
    interface_name = models.CharField(max_length=100, verbose_name='接口名')
    interface_ip = models.GenericIPAddressField(verbose_name='接口IP地址')
    mask = models.GenericIPAddressField(max_length=100, verbose_name='接口掩码')

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.router.routername} " \
               f"| 接口名: {self.interface_name} " \
               f"| 接口IP地址: {self.interface_ip} / {self.mask} )"


class OSPFProcess(models.Model):
    router = models.OneToOneField(Router, related_name='ospfprocess', on_delete='CASCADE')
    processid = models.IntegerField(verbose_name='OSPF进程ID')
    routerid = models.GenericIPAddressField(verbose_name='OSPF Router ID')

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.router.routername} " \
               f"| OSPF进程ID : {self.processid} " \
               f"| Router ID: {self.routerid} )"


class Area(models.Model):
    ospfprocess = models.ForeignKey(OSPFProcess, related_name='area', on_delete='CASCADE')
    area_id = models.IntegerField(verbose_name='区域ID')

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.ospfprocess.router.routername} " \
               f"| OSPF进程ID : {self.ospfprocess.processid} " \
               f"| 区域ID: {self.area_id} )"


class OSPFNetwork(models.Model):
    area = models.ForeignKey(Area, related_name='ospfnetwork', on_delete='CASCADE')
    network = models.GenericIPAddressField(verbose_name='OSPF网络')
    wildmask = models.GenericIPAddressField(verbose_name='OSPF Wild Mask')

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.area.ospfprocess.router.routername} " \
               f"| OSPF进程ID : {self.area.ospfprocess.processid} " \
               f"| 区域ID: {self.area.area_id} " \
               f"| 网络: {self.network} / {self.wildmask} )"


class CPUUsage(models.Model):
    router = models.ForeignKey(Router, related_name='cpuusage', on_delete='CASCADE')
    cpu_useage_percent = models.IntegerField(verbose_name='CPU利用率')
    cpu_useage_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}( 路由器名: {self.router.routername} " \
               f"| 时间 : {self.cpu_useage_datetime} " \
               f"| 利用率: {self.cpu_useage_percent} )"
