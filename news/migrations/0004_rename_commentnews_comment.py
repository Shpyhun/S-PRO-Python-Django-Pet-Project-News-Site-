# Generated by Django 3.2.14 on 2022-08-02 08:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_rename_author_news_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentNews',
            new_name='Comment',
        ),
    ]