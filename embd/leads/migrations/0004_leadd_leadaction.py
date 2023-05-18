# Generated by Django 4.2 on 2023-04-22 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_lead_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('lead_source', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LeadAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_type', models.CharField(max_length=100)),
                ('action_date', models.DateTimeField(auto_now_add=True)),
                ('action_notes', models.TextField()),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leads.leadd')),
            ],
        ),
    ]