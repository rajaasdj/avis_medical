# Generated by Django 5.1.4 on 2025-01-08 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('satisfaction', '0006_delete_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=250)),
            ],
        ),
    ]
