# Generated by Django 5.1.6 on 2025-03-30 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_user_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='products',
        ),
    ]
