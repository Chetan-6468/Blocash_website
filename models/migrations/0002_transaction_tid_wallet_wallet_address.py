# Generated by Django 4.2.1 on 2023-05-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='tid',
            field=models.CharField(default='None', max_length=24),
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallet_address',
            field=models.CharField(default='None', max_length=24),
        ),
    ]
