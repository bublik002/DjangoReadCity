# Generated by Django 4.2.13 on 2024-08-14 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='surname')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='registered')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_staff', models.BooleanField(default=True, verbose_name='is_stuff')),
                ('phone_number', models.CharField(default='77777777777', max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', main.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BooksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=100)),
                ('img', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('score', models.IntegerField(blank=True, null=True)),
                ('num_score', models.IntegerField(blank=True, null=True)),
                ('info_txt', models.CharField(max_length=4000)),
                ('slug_title', models.CharField(blank=True, max_length=500)),
                ('interpreter', models.CharField(blank=True, max_length=100)),
                ('id_book', models.IntegerField(null=True)),
                ('publishing_house', models.CharField(blank=True, max_length=100)),
                ('publishing_brand', models.CharField(blank=True, default='', max_length=100)),
                ('series', models.CharField(blank=True, max_length=100)),
                ('year_of_publishing', models.IntegerField(blank=True, null=True)),
                ('ISBN', models.CharField(blank=True, max_length=100)),
                ('num_page', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(blank=True, max_length=100)),
                ('cover_type', models.CharField(blank=True, max_length=100)),
                ('circulation', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('age_rest', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory1', models.CharField(blank=True, max_length=100)),
                ('subcategory2', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.CharField(max_length=200)),
                ('pluses', models.CharField(blank=True, max_length=200)),
                ('minuses', models.CharField(blank=True, max_length=200)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='review', to='main.booksmodel')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booksmodel',
            name='category',
            field=models.ManyToManyField(to='main.categorymodel'),
        ),
    ]
