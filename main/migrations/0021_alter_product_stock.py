# Generated by Django 4.2.1 on 2023-06-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_productattribute_stock_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.BooleanField(default=True),
        ),
    ]
