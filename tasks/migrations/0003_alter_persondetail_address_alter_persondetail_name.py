# Generated by Django 5.0.4 on 2024-04-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_persondetail_delete_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persondetail',
            name='Address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='persondetail',
            name='Name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]