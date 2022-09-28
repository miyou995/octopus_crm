# Generated by Django 3.2 on 2022-09-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashflow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='acc_type',
            field=models.CharField(blank=True, choices=[('IN', 'In'), ('OU', 'Out')], db_index=True, max_length=2, null=True),
        ),
    ]