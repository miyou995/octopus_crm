# Generated by Django 4.1.3 on 2022-11-26 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cashflow", "0002_account_postal_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="postal_code",
        ),
    ]