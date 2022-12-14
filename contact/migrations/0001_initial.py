from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('annual_revenue', models.DecimalField(blank=True, decimal_places=0, max_digits=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(blank=True, max_length=13, null=True)),
                ('website', models.URLField(blank=True, max_length=250, null=True)),
                ('adress', models.CharField(blank=True, max_length=250, null=True)),
                ('rc_code', models.CharField(blank=True, max_length=150, null=True)),
                ('art_code', models.CharField(blank=True, max_length=150, null=True)),
                ('nif_code', models.CharField(blank=True, max_length=150, null=True)),
                ('nis_code', models.CharField(blank=True, max_length=150, null=True)),
                ('responsible_person', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.CharField(blank=True, max_length=250, null=True)),
                ('company_type', models.CharField(blank=True, choices=[('CL', 'client'), ('F', 'fournisseur'), ('P', 'partenaire'), ('CN', 'concurrent')], max_length=2, null=True)),
                ('project_type', models.CharField(blank=True, choices=[('EC', 'e-commerce'), ('WS', 'web site'), ('WA', 'web app')], max_length=2, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='companies/')),
                ('collab_start', models.DateField(blank=True, null=True)),
                ('created', models.DateField(auto_now=True)),
                ('updated', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
