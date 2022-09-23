# Generated by Django 4.1.1 on 2022-09-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=100)),
                ('s_major', models.CharField(max_length=100)),
                ('s_age', models.IntegerField(default=0)),
                ('s_grade', models.IntegerField(default=0)),
                ('s_gender', models.CharField(max_length=30)),
            ],
        ),
    ]
