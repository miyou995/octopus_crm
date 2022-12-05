# Generated by Django 4.1.3 on 2022-12-05 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0006_remove_billitem_total_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="billitem",
            name="note",
        ),
        migrations.AddField(
            model_name="bill",
            name="note",
            field=models.TextField(blank=True, null=True),
        ),
    ]