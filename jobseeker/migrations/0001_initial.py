# Generated by Django 4.0.3 on 2022-03-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50)),
                ('permanent_address', models.CharField(max_length=500)),
                ('phone_number', models.IntegerField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('education_details', models.CharField(max_length=500)),
                ('fresher', models.BooleanField(default=False)),
                ('dob', models.DateField(auto_now_add=True)),
                ('special_files', models.FileField(upload_to='')),
            ],
        ),
    ]
