# Generated by Django 3.2.13 on 2023-06-15 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_awards_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educations',
            name='time_line',
            field=models.CharField(max_length=100),
        ),
    ]
