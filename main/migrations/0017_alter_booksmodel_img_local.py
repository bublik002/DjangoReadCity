# Generated by Django 5.1.6 on 2025-03-17 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_booksmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='img_local',
            field=models.FileField(blank=True, upload_to='cover'),
        ),
    ]
