# Generated by Django 5.2.1 on 2025-07-24 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_alter_user_verification_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='seller',
            field=models.BooleanField(default=True),
        ),
    ]
