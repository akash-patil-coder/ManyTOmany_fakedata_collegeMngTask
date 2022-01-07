import random
import faker.providers
from random import randint
from django.core.management.base import BaseCommand
from FirstApp.models import Department,Professor,Student
from faker import Faker

dept_list = list(Department.objects.all())

class Provider(faker.providers.BaseProvider):
    def collegeMngDept(self):
        return  self.random_element(dept_list)

    def get_list_departments(self):
        l = randint(1, 3)                                                     #
        return self.random_elements(dept_list, length=l, unique=True)

class Command(BaseCommand):
    help = "Command information"
    def handle(self, *args, **options):
        fake = Faker("en_IN")
        fake.add_provider(Provider)

#        for _ in range(50):
#            name = fake.name()
#            roll_number = fake.unique.random_int(1000,1200)
#            marks = random.randint(10,100)
#            department = fake.collegeMngDept()
#            Student.objects.create(department = department,roll_no = roll_number,stud_name = name,marks = marks)

        for _ in range(15):
            dept = fake.get_list_departments()
            prof_name = fake.name()
            sal = random.randint(50000,150000)
            professor = Professor.objects.create(prof_name=prof_name,sal=sal)
            professor.department.set(dept)
