# Generated by Django 2.0.5 on 2019-03-04 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_authentication', '0006_auto_20190304_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='contact_no',
        ),
    ]
