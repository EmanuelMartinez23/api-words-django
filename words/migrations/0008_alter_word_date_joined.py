# Generated by Django 5.1.4 on 2024-12-22 18:06

import django.db.models.functions.datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0007_alter_word_date_joined_alter_word_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='date_joined',
            field=models.DateField(db_default=django.db.models.functions.datetime.Now()),
        ),
    ]
