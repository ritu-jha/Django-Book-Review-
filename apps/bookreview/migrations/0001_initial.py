# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=20, null=True)),
                ('author', models.TextField(max_length=20, null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'book',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review', models.TextField(max_length=250, null=True)),
                ('rating', models.IntegerField(null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
                ('book', models.ForeignKey(related_name='book', to='bookreview.Book')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField(max_length=20, null=True)),
                ('last_name', models.TextField(max_length=20, null=True)),
                ('email', models.TextField(max_length=20, null=True)),
                ('description', models.TextField(max_length=500, null=True)),
                ('password', models.TextField(max_length=20, null=True)),
                ('created_at', models.DateField(null=True)),
                ('updated_at', models.DateField(null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(related_name='user', to='bookreview.User'),
        ),
    ]
