# Generated by Django 4.1.7 on 2024-03-23 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_applyjob_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='cover_letter',
            field=models.CharField(blank=True, choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('etc', 'etc')], max_length=20, null=True),
        ),
    ]
