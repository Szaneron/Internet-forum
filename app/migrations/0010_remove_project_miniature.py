# Generated by Django 3.0.5 on 2020-04-27 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_project_miniature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='miniature',
        ),
    ]
