# Generated by Django 3.1.4 on 2021-01-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0005_profile_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='group',
        ),
        migrations.AddField(
            model_name='profile',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='user_group', to='auth.Group', verbose_name='user group'),
        ),
    ]
