# Generated by Django 2.1.2 on 2018-11-28 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_vendorqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendorqty',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendor.Product'),
        ),
    ]
