# Generated by Django 5.1.6 on 2025-03-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_booksmodel_age_rest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='age_rest',
            field=models.CharField(blank=True, choices=[('1', 'Нет'), ('2', '6+'), ('3', '12+'), ('4', '16+'), ('5', '18+')], default='1'),
        ),
    ]
