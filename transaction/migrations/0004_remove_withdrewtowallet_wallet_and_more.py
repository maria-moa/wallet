# Generated by Django 4.2.5 on 2023-12-04 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_deposittowallet_amount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrewtowallet',
            name='wallet',
        ),
        migrations.DeleteModel(
            name='DepositToWallet',
        ),
        migrations.DeleteModel(
            name='WithdrewToWallet',
        ),
    ]
