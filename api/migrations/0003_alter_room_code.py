# Generated by Django 4.0 on 2022-03-05 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='', max_length=8, unique=True),
        ),
    ]
