# Generated by Django 2.1.3 on 2018-11-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_remove_vendorprofile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_name',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
