from random import randint
from django.http import JsonResponse
import datetime
import time
from random import randint


# 提供chart刷新的JSON数据
def chart_json(request, chart_type, deviceid):
    if chart_type == 'line' or chart_type == 'bar':
        colors = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d']
        labels = ['2018-8-1', '2018-8-2', '2018-8-3', '2018-8-4', '2018-8-5', '2018-8-6']
        datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
        return JsonResponse({'colors': colors, 'labels': labels, 'datas': datas})
    elif chart_type == 'pie':
        colors = ['#007bff', '#28a745', '#333333', '#c3e6cb', '#dc3545', '#6c757d']
        labels = ['安全', '数据中心', '教主VIP', '路由交换', '无线', '华为']
        datas = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
        return JsonResponse({'colors': colors, 'labels': labels, 'datas': datas})


# 产生每一条线数据的函数
def line_data(name, time_speed_list, color):
    return {
                'symbolSize': 0,  # 这个参数表示在图像上显示的原点大小，为0则不显示
                'symbol': 'circle',
                'name': name,
                'type': 'line',
                'smooth': True,
                'smoothMonotone': True,
                'data': time_speed_list,
                'areaStyle': {
                    'color': color
                },
                'markPoint': {
                    'itemStyle': {
                      'color': color
                    },
                    'data': [
                        {'type': 'max', 'name': '最大值'},
                        {'type': 'min', 'name': '最小值'}
                    ]
                },
                'lineStyle': {
                    'color': color
                },
                'itemStyle': {
                    'color': color
                }
            }


def echarts_final_line_ajax(request):
    # 产生随机数据
    g1_up_time_speed_list = []
    g1_down_time_speed_list = []
    now_time = datetime.datetime.now()
    for i in range(1000):
        g1_up_time_speed_list.append(
            [int(time.mktime((now_time + datetime.timedelta(minutes=i * 30)).timetuple())) * 1000, randint(40, 60)])
        g1_down_time_speed_list.append(
            [int(time.mktime((now_time + datetime.timedelta(minutes=i * 30)).timetuple())) * 1000, randint(30, 70)])
        i += 1

    speed_datas = [line_data('G1 up流量', g1_up_time_speed_list, '#00BFFF'),
                   line_data('G1 down流量', g1_down_time_speed_list, '#FF3300')]

    return JsonResponse({'labelname': '接口速率',
                         'legends': [x['name'] for x in speed_datas],
                         'datas': speed_datas,
                         'starttime': '2019-12-29'})
