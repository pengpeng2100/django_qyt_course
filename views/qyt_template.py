from django.shortcuts import render
from datetime import datetime
from qytapp.models import Department


def qyt_summary(request):
    # mytime = int(datetime.now().strftime("%w"))
    qytsummary = 'QYTANG课程摘要'
    mytime = int(datetime.strptime('2019-12-2', '%Y-%m-%d').strftime("%w"))
    course_list = [course.name for course in Department.objects.all()]
    teacher_list = [{'course': course.name, 'teacher': course.teacher} for course in Department.objects.all()]
    return render(request, 'summary.html', {'qytsummary': qytsummary,
                                            'course_list': course_list,
                                            'teacher_list': teacher_list,
                                            'mytime': mytime})
    # return render(request, 'summary.html', locals())

