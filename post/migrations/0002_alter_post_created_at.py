# Generated by Django 3.2.4 on 2021-06-06 01:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 6, 1, 57, 20, 228858, tzinfo=utc), verbose_name='post time'),
        ),
    ]