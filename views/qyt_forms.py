from qytapp.forms import StudentsForm, EditStudents
from qytapp.models import StudentsDB
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required('qytapp.add_studentsdb')  # 权限控制,只有'qytapp.add_studentsdb'权限的用户才能访问
def addstudent(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        # 如果请求为POST,并且Form校验通过,把新添加的学员信息写入数据库
        if form.is_valid():
            student = StudentsDB(name=request.POST.get('name'),
                                 phone_number=request.POST.get('phone_number'),
                                 qq_number=request.POST.get('qq_number'),
                                 mail=request.POST.get('mail'),
                                 direction=request.POST.get('direction'),
                                 class_adviser=request.POST.get('class_adviser'),
                                 payed=request.POST.get('payed'),
                                 )
            student.save()
            # 写入成功后,显示'学员添加成功'信息!,并且显示空表单
            form = StudentsForm()
            return render(request, 'addstudent.html', {'form': form,
                                                       'successmessage': '学员添加成功!'})

        else:  # 如果Form校验失败,返回客户在Form中输入的内容和报错信息
            # 如果检查到错误,会添加错误内容到form内,例如:<ul class="errorlist"><li>QQ号码已经存在</li></ul>
            return render(request, 'addstudent.html', {'form': form})
    else:  # 如果不是POST,就是GET,表示为初始访问, 显示表单内容给客户
        form = StudentsForm()
        return render(request, 'addstudent.html', {'form': form})


@permission_required('qytapp.view_studentsdb')  # 权限控制,只有'qytapp.view_studentsdb'权限的用户才能访问
def showstudents(request, successmessage=None, errormessage=None):
    all_students = StudentsDB.objects.all()
    students_list = []
    for student in all_students:
        student_dict = {'id': student.id,
                        'name': student.name,
                        'phone_number': student.phone_number,
                        'qq_number': student.qq_number,
                        'mail': student.mail,
                        'direction': student.direction,
                        'class_adviser': student.class_adviser,
                        'payed': '已交费' if student.payed else '未交费',
                        'date': student.edit_date,
                        'delete_url': '/deletestudent/' + str(student.id),
                        'edit_url': '/editstudent/' + str(student.id)}

        students_list.append(student_dict)

    return render(request, 'showstudents.html', {'students_list': students_list,
                                                 'successmessage': successmessage,
                                                 'errormessage': errormessage})


@permission_required('qytapp.delete_studentsdb')  # 权限控制,只有'qytapp.delete_studentsdb'权限的用户才能访问
def deletestudent(request, student_id):
    try:
        delete_student = StudentsDB.objects.get(id=student_id)
        delete_student.delete()
        return showstudents(request, successmessage='学员删除成功!')

    except StudentsDB.DoesNotExist:
        return showstudents(request, errormessage='此学员不存在!')


@permission_required('qytapp.change_studentsdb')  # 权限控制,只有'qytapp.change_studentsdb'权限的用户才能访问
def editstudent(request, student_id):
    try:
        edit_student = StudentsDB.objects.get(id=student_id)
        if request.method == 'POST':
            form = EditStudents(request.POST)
            if form.is_valid():
                edit_student.name = request.POST.get('name')
                edit_student.phone_number = request.POST.get('phone_number')
                edit_student.qq_number = request.POST.get('qq_number')
                edit_student.mail = request.POST.get('mail')
                edit_student.direction = request.POST.get('direction')
                edit_student.class_adviser = request.POST.get('class_adviser')
                edit_student.payed = request.POST.get('payed')
                edit_student.save()
                return showstudents(request, successmessage='编辑学员成功!')

            else:
                return render(request, 'editstudent.html', {'form': form})

        else:
            form = EditStudents(initial={'student_id': edit_student.id,
                                         'name': edit_student.name,
                                         'phone_number': edit_student.phone_number,
                                         'qq_number': edit_student.qq_number,
                                         'mail': edit_student.mail,
                                         'direction': edit_student.direction,
                                         'class_adviser': edit_student.class_adviser,
                                         'payed': edit_student.payed,
                                         })

            return render(request, 'editstudent.html', {'form': form})

    except StudentsDB.DoesNotExist:
        return showstudents(request, errormessage='此学员不存在!')


