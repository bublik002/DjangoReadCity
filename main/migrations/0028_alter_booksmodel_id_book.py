# Generated by Django 5.1.6 on 2025-03-26 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_booksmodel_year_of_publishing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='id_book',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]
