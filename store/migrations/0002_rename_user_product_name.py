# Generated by Django 4.2.6 on 2023-12-10 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user',
            new_name='name',
        ),
    ]
