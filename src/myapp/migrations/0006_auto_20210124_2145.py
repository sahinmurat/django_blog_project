# Generated by Django 3.1.5 on 2021-01-24 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210124_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='p', max_length=10),
        ),
    ]
