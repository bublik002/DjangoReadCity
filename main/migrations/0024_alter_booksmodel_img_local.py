# Generated by Django 5.1.6 on 2025-03-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_booksmodel_publishing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='img_local',
            field=models.FileField(blank=True, upload_to='main/static/img/cover'),
        ),
    ]
