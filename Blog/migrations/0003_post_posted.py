# Generated by Django 4.0.1 on 2022-02-02 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_postcategory_options_post_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted',
            field=models.BooleanField(default=False),
        ),
    ]
