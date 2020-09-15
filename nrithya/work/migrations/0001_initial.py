# Generated by Django 3.0.5 on 2020-07-19 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.TextField(max_length=30)),
                ('phone', models.TextField()),
                ('birthday', models.TextField(max_length=30)),
                ('experience', models.TextField(max_length=30)),
                ('years', models.TextField(max_length=30)),
                ('months', models.TextField(max_length=30)),
                ('currentsalary', models.TextField(max_length=30)),
                ('expectedsalary', models.TextField(max_length=30)),
                ('nameofdegree', models.TextField(max_length=30)),
                ('passyear', models.TextField(max_length=30)),
                ('formsknown', models.TextField(max_length=100)),
            ],
        ),
    ]
