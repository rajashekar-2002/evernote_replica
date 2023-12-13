# Generated by Django 4.2.2 on 2023-06-28 14:08

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('emailverification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=25)),
                ('book_created_on', models.DateTimeField(auto_now_add=True)),
                ('book_last_modified', models.DateTimeField(auto_now=True)),
                ('notebook_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='book_name')),
                ('bookmark_notebook', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emailverification.user')),
            ],
        ),
    ]