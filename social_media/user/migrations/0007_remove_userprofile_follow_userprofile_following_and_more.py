# Generated by Django 4.2.5 on 2023-10-05 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_remove_userprofile_follow_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='follow',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(default=0, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='followers',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='followers',
            field=models.ManyToManyField(default=0, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]