# Generated by Django 2.2.24 on 2021-07-05 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprentices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apprentices',
            name='lesson',
        ),
    ]
