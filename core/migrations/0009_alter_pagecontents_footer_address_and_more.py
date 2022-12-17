# Generated by Django 4.0.4 on 2022-12-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pagecontents_footer_social_icon_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagecontents',
            name='footer_address',
            field=models.CharField(blank=True, default='Lorem ipsum dolor sit amet consectetur, adipiscing elit platea nec.', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pagecontents',
            name='footer_description',
            field=models.CharField(blank=True, default='Lorem ipsum dolor sit amet consectetur adipiscing elit platea convallis tortor, et laoreet posuere nisi suspendisse mollis gravida facilisi fusce cras, augue dictumst tempor imperdiet lacus risus neque elementum nisl.', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pagecontents',
            name='footer_email',
            field=models.CharField(blank=True, default='lorem@lorem.com', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pagecontents',
            name='footer_logo',
            field=models.ImageField(blank=True, default='https://dummyimage.com/99x24', null=True, upload_to='page_contents/'),
        ),
        migrations.AlterField(
            model_name='pagecontents',
            name='footer_phone',
            field=models.CharField(blank=True, default='+123456789', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='pagecontents',
            name='navbar_logo',
            field=models.ImageField(blank=True, default='https://dummyimage.com/99x24', null=True, upload_to='page_contents/'),
        ),
    ]
