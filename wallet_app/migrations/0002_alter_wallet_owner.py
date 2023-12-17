# Generated by Django 4.2.5 on 2023-12-03 05:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wallet_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallet",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="wallets", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
