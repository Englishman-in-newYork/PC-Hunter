# Generated by Django 3.1.4 on 2020-12-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_video_cards_set_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video_cards',
            name='Set_number',
        ),
    ]