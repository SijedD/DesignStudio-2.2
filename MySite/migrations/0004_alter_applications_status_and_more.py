# Generated by Django 4.2.7 on 2023-11-03 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0003_alter_applications_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='Status',
            field=models.CharField(blank=True, default='Новая', max_length=16, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_create',
            field=models.DateField(default=datetime.datetime(2023, 11, 3, 2, 48, 21, 919457), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='time_create',
            field=models.TimeField(default=datetime.datetime(2023, 11, 3, 2, 48, 21, 919470), verbose_name='Время создания'),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
