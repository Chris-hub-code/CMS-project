# Generated by Django 4.0.6 on 2022-07-25 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliant_app', '0002_complaint_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='status',
            field=models.IntegerField(choices=[('Solved', 'Solved'), ('InProgress', 'InProgress'), ('Pending', 'Pending')], null=True),
        ),
    ]
