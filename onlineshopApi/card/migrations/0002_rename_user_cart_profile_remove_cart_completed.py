# Generated by Django 4.0.1 on 2022-01-14 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='user',
            new_name='profile',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='completed',
        ),
    ]
