# Generated by Django 3.1.5 on 2021-01-10 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcm', '0002_auto_20210110_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rack',
            old_name='stored_items_number',
            new_name='stored_items_count',
        ),
    ]
