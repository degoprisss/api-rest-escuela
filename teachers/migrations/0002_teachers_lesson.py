# Generated by Django 2.2.24 on 2021-07-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20210705_1351'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='lesson',
            field=models.ForeignKey(null=True, on_delete=True, to='classes.Classes'),
        ),
    ]
