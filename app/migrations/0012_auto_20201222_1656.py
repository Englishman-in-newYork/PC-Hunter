# Generated by Django 3.1.4 on 2020-12-22 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_ram'),
    ]

    operations = [
        migrations.AddField(
            model_name='ram',
            name='memory_space',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ram',
            name='type_of_ram',
            field=models.CharField(default='none', max_length=20),
        ),
    ]