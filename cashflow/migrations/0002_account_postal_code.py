# Generated by Django 4.1.3 on 2022-11-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cashflow", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="postal_code",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
