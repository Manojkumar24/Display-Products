# Generated by Django 2.1.3 on 2018-12-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20181208_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='vendor',
            field=models.ManyToManyField(to='vendor.VendorProfile'),
        ),
    ]
