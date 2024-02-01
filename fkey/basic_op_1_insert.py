import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qyt_djg.settings')
django.setup()
from fkey.models import User


user1 = User(username='qinke',
             password='Cisc0123',
             email='collinsctk@qytang.com')

user1.save()


user2 = User(username='ender',
             password='Cisc0123',
             email='ender@qytang.com')

user2.save()


user3 = User(username='stu1',
             password='Cisc0123',
             email='stu1@sina.com')

user3.save()