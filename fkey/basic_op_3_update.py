import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()
from fkey.models import User

user_get = User.objects.get(username='qinke')
print(user_get.email)
user_get.email = 'qinke@qytang.com'
user_get.save()

user_get = User.objects.get(username='qinke')
print(user_get.email)
