# Generated by Django 2.1.1 on 2018-09-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm_1', '0002_auto_20180913_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url_type', models.SmallIntegerField(choices=[(0, 'absolute'), (1, 'dynamic')])),
                ('url_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='menus',
            unique_together={('name', 'url_name')},
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm_1.Menus'),
        ),
    ]
