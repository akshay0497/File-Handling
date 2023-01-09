# Generated by Django 3.2.16 on 2023-01-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileHandling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=10, verbose_name='Index')),
                ('user_id', models.CharField(max_length=200, verbose_name='User Id')),
                ('first_name', models.CharField(max_length=250, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=250, verbose_name='Last Name')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Id')),
                ('phone', models.CharField(max_length=25, verbose_name='Phone Numnber')),
                ('d_o_b', models.CharField(max_length=15, verbose_name='Dat of Birth')),
                ('job_title', models.CharField(max_length=300, verbose_name='Job Title')),
            ],
        ),
    ]
