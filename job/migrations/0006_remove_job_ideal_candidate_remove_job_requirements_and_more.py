# Generated by Django 4.1.7 on 2024-03-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_applyjob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='ideal_candidate',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requirements',
        ),
        migrations.AddField(
            model_name='job',
            name='Company_Benefits',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='Employment_Type',
            field=models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('etc', 'etc')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='How_to_Apply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='application_Deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='required_qualifications',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='responsibilities',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary_Range',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
