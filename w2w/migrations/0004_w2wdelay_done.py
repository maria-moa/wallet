# Generated by Django 4.2.5 on 2023-12-04 12:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("w2w", "0003_w2wdelay"),
    ]

    operations = [
        migrations.AddField(
            model_name="w2wdelay",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
