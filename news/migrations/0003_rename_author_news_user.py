# Generated by Django 3.2.14 on 2022-08-02 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20220801_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='author',
            new_name='user',
        ),
    ]