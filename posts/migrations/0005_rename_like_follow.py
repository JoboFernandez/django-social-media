# Generated by Django 4.1 on 2022-08-17 09:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_alter_comment_options_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='Follow',
        ),
    ]
