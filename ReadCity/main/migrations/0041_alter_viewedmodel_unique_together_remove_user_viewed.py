# Generated by Django 5.2.1 on 2025-07-14 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_rename_viewed_viewedmodel'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='viewedmodel',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='viewed',
        ),
    ]
