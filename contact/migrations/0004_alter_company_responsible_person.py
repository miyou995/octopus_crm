# Generated by Django 3.2 on 2022-11-09 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0003_auto_20221107_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='responsible_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to=settings.AUTH_USER_MODEL, verbose_name='Responsable de la société'),
        ),
    ]