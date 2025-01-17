# Generated by Django 5.1.4 on 2025-01-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satisfaction', '0008_visite_ref_pat_visite_service_visite_specialite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avis',
            name='feedback',
        ),
        migrations.AlterField(
            model_name='visite',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Code Visite'),
        ),
        migrations.AlterField(
            model_name='visite',
            name='ref_pat',
            field=models.CharField(max_length=50, verbose_name='Référence Patient'),
        ),
        migrations.AlterField(
            model_name='visite',
            name='service',
            field=models.CharField(max_length=50, verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='visite',
            name='specialite',
            field=models.CharField(max_length=50, verbose_name='Spécialité'),
        ),
    ]
