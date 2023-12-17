# Generated by Django 4.2.5 on 2023-09-20 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet_app', '0001_initial'),
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrewToWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('tracker_id', models.CharField(default=None, max_length=255, null=True, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Approved'), (1, 'Rejected'), (2, 'Waiting')], default=2)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_app.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='DepositToWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('tracker_id', models.CharField(default=None, max_length=255, null=True, unique=True)),
                ('status', models.IntegerField(choices=[(0, 'Approved'), (1, 'Rejected'), (2, 'Waiting')], default=2)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet_app.wallet')),
            ],
        ),
    ]
