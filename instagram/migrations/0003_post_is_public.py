# Generated by Django 4.0.1 on 2022-01-26 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
