from django.db import models
from django.db.models import Model, CharField, ForeignKey, IntegerField, DateField


class Company(Model):
    name = CharField(max_length=256)
    location = CharField(max_length=128)
    logo = CharField(max_length=2048, null=True)
    description = CharField(max_length=2048)
    employee_count = IntegerField()


class Specialty(Model):
    code = CharField(max_length=128)
    title = CharField(max_length=256)
    picture = CharField(max_length=2048, null=True)


class Vacancy(Model):
    title = CharField(max_length=256)
    specialty = ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = CharField(max_length=2048)
    description = CharField(max_length=2048)
    salary_min = IntegerField()
    salary_max = IntegerField()
    published_at = DateField()
