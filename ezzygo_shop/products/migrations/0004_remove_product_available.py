# Generated by Django 4.2.3 on 2023-07-04 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_order_available_remove_order_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
    ]