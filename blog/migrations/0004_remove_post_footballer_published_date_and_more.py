# Generated by Django 5.0.9 on 2024-11-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_post_post_footballer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_footballer',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post_footballer',
            name='footballer_curr_club',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='post_footballer',
            name='footballer_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]