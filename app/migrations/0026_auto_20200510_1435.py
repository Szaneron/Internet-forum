# Generated by Django 3.0.5 on 2020-05-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20200510_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='miniature',
            field=models.ImageField(default='static/arduino.jpg', upload_to='static/'),
        ),
    ]
