# Generated by Django 2.2.2 on 2019-06-20 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20190621_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
    ]
