# Generated by Django 4.0.1 on 2022-02-02 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=101)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=101)),
                ('image', models.ImageField(blank=True, upload_to='post_pics')),
                ('title_slug', models.SlugField(max_length=101)),
                ('content', models.TextField(max_length=500)),
                ('summary', models.TextField(max_length=5001)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Blog.postcategory')),
            ],
        ),
    ]