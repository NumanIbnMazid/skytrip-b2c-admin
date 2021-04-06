# Generated by Django 3.1.4 on 2021-03-10 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0005_couponsetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='couponsetting',
            name='coupon_type',
            field=models.SmallIntegerField(choices=[('0', 'Percentage'), ('1', 'Fixed Amount')], default=0, verbose_name='coupon type'),
        ),
    ]
