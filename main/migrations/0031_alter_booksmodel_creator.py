# Generated by Django 5.1.6 on 2025-03-30 13:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_remove_user_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Продавец', to=settings.AUTH_USER_MODEL),
        ),
    ]
