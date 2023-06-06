# Generated by Django 4.2.1 on 2023-06-06 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_addressdetailmodel_studentdetailmodel_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetailmodel',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_detail_address', to='student.addressdetailmodel'),
        ),
        migrations.AlterField(
            model_name='studentdetailmodel',
            name='contact_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_detail_contact_info', to='student.studentcontactdetailmodel'),
        ),
    ]
