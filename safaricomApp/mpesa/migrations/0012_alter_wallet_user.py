# Generated by Django 4.2.7 on 2024-01-10 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mpesa', '0011_alter_wallet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to='mpesa.userprofile'),
        ),
    ]
