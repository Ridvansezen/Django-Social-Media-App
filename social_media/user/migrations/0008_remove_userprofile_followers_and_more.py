# Generated by Django 4.2.5 on 2023-10-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_userprofile_follow_userprofile_following_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='following',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
