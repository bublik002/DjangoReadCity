# Generated by Django 5.2.1 on 2025-07-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='viewed',
            field=models.ManyToManyField(blank=True, max_length=10, related_name='viewed', to='main.booksmodel'),
        ),
    ]
