# Generated by Django 4.2.6 on 2023-10-06 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_contact_employee_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
    ]
