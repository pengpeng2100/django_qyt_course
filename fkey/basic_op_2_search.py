import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()
from fkey.models import User

# 搜索特定用户
user_get = User.objects.get(username='qinke')
print(user_get)
print(user_get.password)

# 处理get的问题
# 找不到条目
try:
    user_get = User.objects.get(username='qinke1')
except User.DoesNotExist:
    print('用户未找到')

# 找到多个条目
try:
    user_get = User.objects.get(password='Cisc0123')
except User.MultipleObjectsReturned:
    print('找到多个条目')

# 获取所有用户
user_all = User.objects.all()

for user in user_all:
    print(user)

# 通过过滤找到用户, 找到一个,没找到,或者找到多个,并不会产生错误!
users_filter = User.objects.filter(password='Cisc0123')
for user in users_filter:
    print(user)
