# Generated by Django 5.1.1 on 2024-10-07 19:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamento',
            name='descricao',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lancamento',
            name='tipo',
            field=models.CharField(choices=[('credito', 'Crédito'), ('debito', 'Débito')], max_length=7),
        ),
    ]
