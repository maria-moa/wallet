# Generated by Django 4.2.5 on 2023-12-23 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wallet_app", "0001_initial"),
        ("transaction", "0004_alter_action_action_type_alter_action_created_at_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="wallet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="actions", to="wallet_app.wallet"
            ),
        ),
    ]
