# Generated by Django 5.1.4 on 2024-12-23 12:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='accountability',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='awareness',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='gratitude',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='gratitude_blessings',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='humility',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='interactions',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='patience',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='personal_improvement',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='spiritual_practice',
        ),
        migrations.AddField(
            model_name='entry',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='intention',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]