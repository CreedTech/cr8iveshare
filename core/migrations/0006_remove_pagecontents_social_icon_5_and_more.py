# Generated by Django 4.0.4 on 2022-12-17 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_pagecontents_social_icon_url_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagecontents',
            name='social_icon_5',
        ),
        migrations.RemoveField(
            model_name='pagecontents',
            name='social_icon_url_5',
        ),
        migrations.RemoveField(
            model_name='pagecontents',
            name='updated',
        ),
    ]
