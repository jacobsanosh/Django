# Generated by Django 4.1.4 on 2023-03-17 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webpage',
            old_name='topic',
            new_name='category',
        ),
    ]
