# Generated by Django 4.1.7 on 2023-03-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True)),
                ('Date', models.DateField()),
                ('AssignTo', models.TextField(blank=True, max_length=100)),
                ('Completed', models.BooleanField()),
            ],
        ),
    ]
