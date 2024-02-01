import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()
from fkey.models import User

# 删除所有
# User.objects.all().delete()

# 删除filter找到的所有条目
User.objects.filter(password='Cisc0123', username='qinke').delete()

# 删除特定条目
User.objects.get(username='ender').delete()
