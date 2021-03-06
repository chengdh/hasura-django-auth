# Generated by Django 3.2.12 on 2022-02-21 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_organization_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frontend_router_path', models.CharField(max_length=200, verbose_name='路径')),
                ('frontend_router_name', models.CharField(help_text='对应前端router名称', max_length=200, verbose_name='类别')),
                ('frontend_router_redirect', models.CharField(blank=True, max_length=200, null=True, verbose_name='重定向path')),
                ('frontend_router_meta_title', models.CharField(max_length=200, verbose_name='类别')),
                ('frontend_router_meta_icon', models.CharField(blank=True, max_length=200, null=True, verbose_name='显示图标')),
                ('rank', models.IntegerField(default=1, verbose_name='排序')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('note', models.TextField(blank=True, null=True, verbose_name='备注')),
            ],
        ),
        migrations.DeleteModel(
            name='FunctionCateogry',
        ),
        migrations.AddField(
            model_name='systemfunctionoperate',
            name='system_function',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.systemfunction', verbose_name='所属功能'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='role',
            name='system_function_operates',
            field=models.ManyToManyField(blank=True, to='api.SystemFunctionOperate', verbose_name='角色具有的权限'),
        ),
        migrations.AddField(
            model_name='systemfunction',
            name='function_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.functioncategory', verbose_name='所属类别'),
            preserve_default=False,
        ),
    ]
