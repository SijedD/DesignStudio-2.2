# Generated by Django 4.2.7 on 2023-11-03 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0004_alter_applications_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='Status',
        ),
        migrations.AlterField(
            model_name='applications',
            name='date_create',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='time_create',
            field=models.TimeField(default=datetime.datetime.now, verbose_name='Время создания'),
        ),
        migrations.AddField(
            model_name='applications',
            name='status',
            field=models.CharField(blank=True, choices=[('Новая', 'Новая'), ('Принято в работу', 'Принято в работу'), ('Выполнено', 'Выполнено')], default='Новая', max_length=16, verbose_name='Статус'),
        ),
    ]
