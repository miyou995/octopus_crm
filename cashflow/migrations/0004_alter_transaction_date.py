# Generated by Django 4.1.3 on 2023-01-25 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cashflow", "0003_alter_transaction_account_sd"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]