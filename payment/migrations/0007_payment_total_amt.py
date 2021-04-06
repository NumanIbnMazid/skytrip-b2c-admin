# Generated by Django 3.1.4 on 2021-01-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_remove_payment_total_amt'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='total_amt',
            field=models.FloatField(default=100, verbose_name='total amount'),
            preserve_default=False,
        ),
    ]
