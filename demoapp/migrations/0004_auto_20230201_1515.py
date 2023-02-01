# Generated by Django 3.2.16 on 2023-02-01 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_delete_contactdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]