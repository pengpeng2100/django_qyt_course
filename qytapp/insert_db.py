import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()

from qytapp.models import Department
import json

# class Department(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=False)
#     summary = models.CharField(max_length=10000, blank=True, null=True)
#     teacher = models.CharField(max_length=100, blank=False)
#     method = models.CharField(max_length=100, blank=False)
#     characteristic = models.CharField(max_length=100, blank=True)
#     if_provide_lab = models.BooleanField(default=True)
#     detail = models.CharField(max_length=10000, blank=False)


# insert data
depart1 = Department(name='安全',
                     summary='主要讲解网络安全知识',
                     teacher='现任明教教主',
                     method='在线,网真,本地',
                     characteristic='加入黑客技术',
                     if_provide_lab=True,
                     detail=json.dumps(['FW', 'VPN', 'IDS', 'Hacker']))
depart1.save()


depart2 = Department(name='教主VIP',
                     summary='主要讲解各种新技术',
                     teacher='秦柯',
                     method='在线,网真,本地',
                     # characteristic='加入黑客技术',
                     if_provide_lab=False,
                     detail=json.dumps(['PA', 'Python', 'AWS']))
depart2.save()


depart3 = Department(name='无线',
                     summary='主要讲解无线技术',
                     teacher='秦柯',
                     method='在线,网真,本地',
                     # characteristic='加入黑客技术',
                     if_provide_lab=True,
                     detail=json.dumps(['WIRNA', 'WLC', 'PI']))
depart3.save()


# search Data
# try:
#     depart = Department.objects.get(teacher='秦柯')
#     print(depart)
# except Department.DoesNotExist:
#     print('没有找到!')
# except Department.MultipleObjectsReturned:
#     print('找到多个条目!')


# departs = Department.objects.filter(teacher='秦柯', name='无线')
#
# for depart_obj in departs:
#     print(depart_obj)


# wir_depart = Department.objects.get(teacher='秦柯', name='无线')
#
# print(wir_depart.summary)
# print(json.loads(wir_depart.detail))

# update data
# wir_depart = Department.objects.get(teacher='秦柯', name='无线')
# print(wir_depart.summary)
# wir_depart.summary = '主要讲解最新的无线技术'
# wir_depart.save()
#
# wir_depart = Department.objects.get(teacher='秦柯', name='无线')
# print(wir_depart.summary)


# delete data
# wir_depart = Department.objects.get(teacher='秦柯', name='无线')
# wir_depart.delete()

# all_departs = Department.objects.all()
#
# for x in all_departs:
#     print(x)

# Department.objects.all().delete()
