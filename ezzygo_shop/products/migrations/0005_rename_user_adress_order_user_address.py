# Generated by Django 4.2.3 on 2023-07-04 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_product_available'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_adress',
            new_name='user_address',
        ),
    ]
