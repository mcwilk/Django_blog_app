# Generated by Django 2.2.12 on 2020-04-22 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='creation_date',
            new_name='created_on',
        ),
    ]
