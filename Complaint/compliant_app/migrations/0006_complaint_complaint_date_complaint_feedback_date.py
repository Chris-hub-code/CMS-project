# Generated by Django 4.0.6 on 2022-07-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliant_app', '0005_alter_complaint_description_alter_complaint_subject_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Complaint_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='Feedback_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
