# Generated by Django 3.2.12 on 2022-02-22 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220222_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemfunctionoperate',
            name='code',
            field=models.CharField(default='code', max_length=200, verbose_name='操作代码'),
            preserve_default=False,
        ),
    ]
