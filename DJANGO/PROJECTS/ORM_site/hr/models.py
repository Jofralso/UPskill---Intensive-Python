from django.db import models
from datetime import date


class Contact(models.Model):
    phone = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.phone


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Compensation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
        null=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    compensations = models.ManyToManyField(Compensation)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Job(models.Model):
    title = models.CharField(max_length=255)
    employees = models.ManyToManyField(Employee, through='Assignment')

    def __str__(self):
        return self.title


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    begin_date = models.DateField()
    end_date = models.DateField(default=date(9999, 12, 31))


# from time
# h1 = PositionHistory(employee=e1,position=p1, begin_date=date(2019,1,1), end_date=date(2021,12,31))
# h1.save()

# h2 = PositionHistory(employee=e1,position=p2, begin_date=date(2022,1,1))
# h2.save()


# h3 = PositionHistory(employee=e2, position=p1, begin_date=date(2019, 3, 1))
# h3.save()
