# Generated by Django 4.0.1 on 2022-01-21 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_fruit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fruit',
            old_name='fruit',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='region',
            old_name='region',
            new_name='name',
        ),
    ]
