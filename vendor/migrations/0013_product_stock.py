# Generated by Django 2.2.5 on 2019-11-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0012_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
