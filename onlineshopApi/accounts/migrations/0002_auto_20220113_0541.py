# Generated by Django 3.2 on 2022-01-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(blank=True, choices=[(7, 'Qashqadaryo'), (12, 'Buxoro'), (9, 'Fargona'), (8, 'Xorazm'), (10, 'Jizzax'), (6, 'Samarqand'), (2, 'Surxondaryo'), (11, 'Toshkent vil'), (1, 'Toshkent:'), (5, 'Navoi'), (3, 'Andijon'), (4, 'Namangan')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True),
        ),
    ]