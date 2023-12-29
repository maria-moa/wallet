# Generated by Django 4.2.5 on 2023-12-23 23:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_config", "0002_delete_userconfig"),
    ]

    operations = [
        migrations.AddField(
            model_name="config",
            name="max",
            field=models.PositiveBigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name="config",
            name="min",
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]