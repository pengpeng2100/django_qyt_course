"""qyt_djg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views import index, qyt_template, qyt_course_detail, qyt_forms, qyt_charts, qyt_ajax, qyt_login

urlpatterns = [
    path('admin/', admin.site.urls),
    # 首页
    path('', index.qytang_index),
    # 课程摘要
    path('summary', qyt_template.qyt_summary),

    # 课程详细信息的静态路由
    # path('sec', qyt_course_detail.sec_course),
    # path('vip', qyt_course_detail.vip_course)

    # 课程详细信息的动态路由
    path('depart/<str:department_name>', qyt_course_detail.dynamic_course),

    # 添加学员
    path('addstudent', qyt_forms.addstudent),

    # 查看与搜索学员
    path('showstudents', qyt_forms.showstudents),

    # 删除学员
    path('deletestudent/<int:student_id>', qyt_forms.deletestudent),

    # 编辑学员
    path('editstudent/<int:student_id>', qyt_forms.editstudent),

    # charts数据源自于Django
    path('data_from_django', qyt_charts.data_from_django),

    # echarts数据源自于Django
    path('echarts_from_django', qyt_charts.echarts_from_django),

    # echarts终极线形图
    path('echarts_final_line', qyt_charts.echarts_final_line),

    # echarts终极线形图Ajax
    path('ajax/echarts_final_line_ajax', qyt_ajax.echarts_final_line_ajax),

    # charts数据源自于ajax
    path('data_from_ajax', qyt_charts.data_from_ajax),

    # ajax后台
    path('ajax/<str:chart_type>/<int:deviceid>', qyt_ajax.chart_json),

    # 登录页面
    path('accounts/login/', qyt_login.qyt_login),
    # 注销页面
    path('accounts/logout/', qyt_login.qyt_logout),
]
