# Generated by Django 3.1.2 on 2021-06-17 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instmini', '0002_auto_20210617_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_at']},
        ),
    ]