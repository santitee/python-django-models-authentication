# Generated by Django 2.2.9 on 2022-03-21 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20220321_2306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tag',
            new_name='tags',
        ),
    ]
