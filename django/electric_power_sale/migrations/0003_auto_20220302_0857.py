# Generated by Django 3.2.12 on 2022-03-02 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric_power_sale', '0002_customer_use_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='elect_level',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='电压等级'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='transformer_volume',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='变压器容量'),
        ),
    ]
