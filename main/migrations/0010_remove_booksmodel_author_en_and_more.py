# Generated by Django 5.1.6 on 2025-02-23 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_booksmodel_author_en_booksmodel_author_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksmodel',
            name='author_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='author_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='cover_type_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='cover_type_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='info_txt_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='info_txt_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='interpreter_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='interpreter_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='publishing_brand_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='publishing_brand_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='publishing_house_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='publishing_house_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='series_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='series_ru',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='booksmodel',
            name='title_ru',
        ),
    ]
