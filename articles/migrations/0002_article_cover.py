# Generated by Django 3.2.8 on 2021-10-28 17:56

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover',
            field=models.ImageField(default=1, upload_to=articles.models.user_directory_path),
            preserve_default=False,
        ),
    ]
