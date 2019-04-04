# Generated by Django 2.1 on 2019-04-04 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0017_remove_server_disk_capacity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disk_name', models.CharField(help_text='设备名', max_length=16, verbose_name='设备名')),
                ('capacity', models.DecimalField(blank=True, decimal_places=2, help_text='容量大小(GB)', max_digits=10, null=True, verbose_name='容量大小(GB)')),
                ('server', models.ForeignKey(blank=True, help_text='所属服务器', null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Server', verbose_name='所属服务器')),
            ],
            options={
                'verbose_name': '硬盘',
                'verbose_name_plural': '硬盘',
                'ordering': ['id'],
            },
        ),
    ]
