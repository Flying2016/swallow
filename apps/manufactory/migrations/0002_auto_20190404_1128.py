# Generated by Django 2.1 on 2019-04-04 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufactory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='product_name',
            field=models.CharField(help_text='型号名称', max_length=128, verbose_name='型号名称'),
        ),
    ]
