# Generated by Django 4.1.7 on 2024-03-26 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0014_remove_job_salary_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
