# Generated by Django 5.1.3 on 2024-11-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_student_address_alter_student_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.BigIntegerField(),
        ),
    ]
