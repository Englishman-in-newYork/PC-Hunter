# Generated by Django 3.1.4 on 2021-01-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210126_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='name_of_ram',
            field=models.CharField(default='none', max_length=40),
        ),
    ]
