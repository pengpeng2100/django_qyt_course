from django.shortcuts import render
from datetime import datetime
from qytapp.models import Department
import json
from django.contrib.auth.decorators import login_required


# @login_required()
# def sec_course(request):
#     # sec = {'方向': '安全',
#     #        '摘要': '主要讲解网络安全知识',
#     #        '授课老师': '现任明教教主',
#     #        '授课方式': '在线,网真,本地',
#     #        '课程特色': '加入黑客技术',
#     #        '是否提供实验环境': True,
#     #        '具体课程': ['FW', 'VPN', 'IDS', 'Hacker']}
#
#     department = Department.objects.get(name='安全')
#     depart = {'方向': department.name,
#               '摘要': department.summary,
#               '授课老师': department.teacher,
#               '授课方式': department.method,
#               '课程特色': department.characteristic if department.characteristic else False,
#               '是否提供实验环境': department.if_provide_lab,
#               '具体课程': json.loads(department.detail)}
#     return render(request, 'course_detail.html', {'courseinfo': depart,
#                                                   'qyt_date': datetime.now()})
#
#
# @login_required()
# def vip_course(request):
#     department = Department.objects.get(name='教主VIP')
#     depart = {'方向': department.name,
#               '摘要': department.summary,
#               '授课老师': department.teacher,
#               '授课方式': department.method,
#               '课程特色': department.characteristic if department.characteristic else False,
#               '是否提供实验环境': department.if_provide_lab,
#               '具体课程': json.loads(department.detail)}
#     return render(request, 'course_detail.html', {'courseinfo': depart,
#                                                   'qyt_date': datetime.now()})


@login_required()
def dynamic_course(request, department_name):
    if department_name == 'sec':
        department = Department.objects.get(name='安全')
    elif department_name == 'vip':
        department = Department.objects.get(name='教主VIP')
    else:
        department = Department.objects.get(name='安全')

    depart = {'方向': department.name,
              '摘要': department.summary,
              '授课老师': department.teacher,
              '授课方式': department.method,
              '课程特色': department.characteristic if department.characteristic else False,
              '是否提供实验环境': department.if_provide_lab,
              '具体课程': json.loads(department.detail)}
    return render(request, 'course_detail.html', {'courseinfo': depart,
                                                  'qyt_date': datetime.now()})
