# Generated by Django 4.0.6 on 2022-07-08 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempuser',
            name='room_name',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]