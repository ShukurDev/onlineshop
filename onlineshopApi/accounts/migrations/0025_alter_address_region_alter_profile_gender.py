# Generated by Django 4.0.1 on 2022-01-15 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_address_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='region',
            field=models.CharField(choices=[('Toshkent', 'Toshkent:'), ('Surxondaryo', 'Surxondaryo'), ('Jizzax', 'Jizzax'), ('Andijon', 'Andijon'), ('Xorazm', 'Xorazm'), ('Toshkent vil', 'Toshkent vil'), ('Samarqand', 'Samarqand'), ('Navoi', 'Navoi'), ('Fargona', 'Fargona'), ('Namangan', 'Namangan'), ('Qashqadaryo', 'Qashqadaryo'), ('Buxoro', 'Buxoro')], default='empty', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=50, null=True),
        ),
    ]
