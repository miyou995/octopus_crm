# Generated by Django 3.2 on 2022-09-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20220914_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='project_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]