# Generated by Django 4.0.3 on 2022-03-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0007_alter_jobseeker_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='key_skill',
            field=models.CharField(default='', max_length=255),
        ),
    ]
