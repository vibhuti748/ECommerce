# Generated by Django 4.2.2 on 2023-06-16 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_cartorder_cartorderitems'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartorder',
            options={'verbose_name_plural': '8. Orders'},
        ),
        migrations.AlterModelOptions(
            name='cartorderitems',
            options={'verbose_name_plural': '9. Order Items'},
        ),
    ]
