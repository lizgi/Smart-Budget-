# Generated by Django 4.0.1 on 2022-01-11 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0002_auto_20220108_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userincome',
            options={'ordering': ['-date']},
        ),
    ]
