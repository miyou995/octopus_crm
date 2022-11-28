# Generated by Django 3.2 on 2022-11-27 14:22

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0002_company_postal_code_alter_company_company_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
                ('started_date', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('project_type', models.CharField(blank=True, choices=[('E-COMMERCE', 'e-commerce'), ('WEB SITE', 'web site'), ('WEB APP', 'web app')], max_length=20, null=True)),
                ('contract', models.CharField(blank=True, choices=[('HOSTING', 'hosting'), ('ANNUAL', 'annual'), ('SEMI-ANNUAL', 'semi-annual'), ('QUARTERLY', 'quarterly'), ('ADVERTISEMENT', 'advertisement')], max_length=20, null=True)),
                ('contract_expiration', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('CF', 'Confirm'), ('CP', 'Completed'), ('PE', 'Pending'), ('CA', 'Cancelled')], max_length=2, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='contact.company', verbose_name='client')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_managers', to=settings.AUTH_USER_MODEL, verbose_name='manager')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, choices=[('low', 'LOW'), ('meduim', 'MEDUIM'), ('high', 'HIGH')], max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervised_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_responsible', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_member_of_team', to=settings.AUTH_USER_MODEL, verbose_name='member_of_team')),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('member', models.ManyToManyField(through='project.TeamMember', to=settings.AUTH_USER_MODEL, verbose_name='member')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_of_project', to='project.project', verbose_name='project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_to_team', to='project.task', verbose_name='task')),
            ],
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_member_of_project', to='project.teams', verbose_name='team_of_project'),
        ),
    ]