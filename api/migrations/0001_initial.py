# Generated by Django 3.0.5 on 2020-06-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trial_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=200, null=True)),
                ('time', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
