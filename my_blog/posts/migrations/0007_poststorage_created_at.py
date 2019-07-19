# Generated by Django 2.1.1 on 2019-07-19 14:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_poststorage_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='poststorage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
