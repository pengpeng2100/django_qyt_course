from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    summary = models.CharField(max_length=10000, blank=True, null=True)
    teacher = models.CharField(max_length=100, blank=False)
    method = models.CharField(max_length=100, blank=False)
    characteristic = models.CharField(max_length=100, blank=True, null=True)
    if_provide_lab = models.BooleanField(default=True)
    detail = models.CharField(max_length=10000, blank=False)

    def __str__(self): 
        return f"{self.__class__.__name__}(Name: {self.name} | Teacher: {self.teacher})"


class StudentsDB(models.Model):
    name = models.CharField(max_length=100, verbose_name='学员姓名')
    # 电话号码,校验以1开头的11位数字,最大长度为11,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="Phone number must be entered in the format: '13911153335'. 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=False, unique=True)

    # QQ号,校验5到20位的数字,最大长度为20,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ number must be entered in the format: '605658506'. 5-20 digits allowed.")
    qq_number = models.CharField(validators=[qq_regex], max_length=20, blank=False, unique=True)
    # 邮件,EmailField会校验邮件格式,最大长度50, 可以为空(注意:并没有min_length这个控制字段)
    mail = models.EmailField(max_length=100, unique=True, verbose_name='学员邮件')
    # 学习方向,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = models.CharField(max_length=5, choices=direction_choices)

    # 班主任,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = models.CharField(max_length=2, choices=class_adviser_choices)

    # 缴费情况,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    payed_choices = ((True, '已缴费'), (False, '未交费'))
    payed = models.BooleanField(default=False, choices=payed_choices)
    # 修改时间
    edit_date = models.DateField(auto_now=True, verbose_name='修改时间')

    def __str__(self):
        return f"{self.__class__.__name__}(Name: {self.name} | Direction: {self.direction} | Email: {self.mail} | Phone: {self.phone_number})"
