# Generated by Django 3.1.4 on 2021-02-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnr', '0025_auto_20210211_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pnrcarriercodestats',
            name='pnr_list',
            field=models.JSONField(blank=True, default=list, null=True, verbose_name='pnr list'),
        ),
    ]
