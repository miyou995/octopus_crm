# Generated by Django 3.2 on 2022-10-30 14:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0009_alter_project_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='team'),
        ),
    ]
