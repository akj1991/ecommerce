# Generated by Django 4.0.1 on 2022-06-16 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobile_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(max_length=20)),
                ('brand', models.TextField(max_length=20)),
                ('rate', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'mobiledetails',
            },
        ),
    ]
