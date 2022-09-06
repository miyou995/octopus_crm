# Generated by Django 3.2 on 2022-09-04 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250)),
                ('acc_type', models.CharField(choices=[('IN', 'In'), ('OU', 'Out')], db_index=True, max_length=2, null=True)),
                ('actif', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project.project')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tr_type', models.CharField(blank=True, choices=[('PA', 'paiement'), ('SA', 'salaire '), ('CR', 'creance'), ('CH', 'charges'), ('AL', 'allouer')], max_length=2, null=True)),
                ('other', models.CharField(blank=True, max_length=254, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('note', models.CharField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('account_rc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='cashflow.account')),
                ('account_sd', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='cashflow.account')),
                ('made_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='made_transactions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
