# Generated by Django 3.2.9 on 2021-12-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('lives_in', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
