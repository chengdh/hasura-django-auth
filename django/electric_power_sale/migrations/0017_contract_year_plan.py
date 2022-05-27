# Generated by Django 3.2.12 on 2022-05-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_power_sale', '0016_auto_20220327_0254'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='year_plan',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=20, verbose_name='年度签约电量(兆瓦时)'),
        ),
    ]
