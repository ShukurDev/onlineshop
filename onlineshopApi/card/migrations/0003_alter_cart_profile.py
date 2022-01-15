# Generated by Django 4.0.1 on 2022-01-15 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_alter_address_region'),
        ('card', '0002_rename_user_cart_profile_remove_cart_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='accounts.profile'),
        ),
    ]
