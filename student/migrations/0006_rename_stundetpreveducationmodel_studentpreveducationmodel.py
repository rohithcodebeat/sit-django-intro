# Generated by Django 4.2.1 on 2023-06-07 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_stundetpreveducationmodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StundetPrevEducationModel',
            new_name='StudentPrevEducationModel',
        ),
    ]
