# Generated by Django 2.1.3 on 2018-11-26 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_vendorprofile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorprofile',
            name='address',
        ),
    ]
