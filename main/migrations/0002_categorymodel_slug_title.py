# Generated by Django 4.2.13 on 2024-08-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug_title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]