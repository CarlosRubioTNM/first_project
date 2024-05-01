import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

##Fake pop script
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def add_user():
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_mail = fakegen.email()
    t = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_mail)[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #Get the topic for the entry
        x = add_user()

if __name__ == '__main__':
    print("Populating script")
    populate(30)
    print("Finished")