# Generated by Django 3.1.4 on 2020-12-18 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_set', models.CharField(max_length=100)),
                ('identicator', models.IntegerField(default=0)),
            ],
        ),
    ]
