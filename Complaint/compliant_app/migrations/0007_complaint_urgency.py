# Generated by Django 4.0.6 on 2022-07-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compliant_app', '0006_complaint_complaint_date_complaint_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Urgency',
            field=models.CharField(blank=True, choices=[('VERY URGENT', 'VERY URGENT'), ('URGENT', 'URGENT'), ('URGENT', 'URGENT')], max_length=200, null=True),
        ),
    ]
