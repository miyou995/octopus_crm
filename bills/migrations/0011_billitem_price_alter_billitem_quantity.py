# Generated by Django 4.1.3 on 2022-11-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bills", "0010_alter_invoice_bill_ptr_alter_proforma_bill_ptr"),
    ]

    operations = [
        migrations.AddField(
            model_name="billitem",
            name="price",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="billitem",
            name="quantity",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]