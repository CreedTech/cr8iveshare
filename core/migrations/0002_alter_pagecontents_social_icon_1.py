# Generated by Django 4.0.4 on 2022-12-17 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontents',
            name='social_icon_1',
            field=models.CharField(blank=True, default='twitter', max_length=30, null=True),
        ),
    ]
