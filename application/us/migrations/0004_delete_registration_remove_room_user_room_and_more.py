# Generated by Django 4.0.2 on 2022-02-27 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0003_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='registration',
        ),
        migrations.RemoveField(
            model_name='room',
            name='user_room',
        ),
        migrations.DeleteModel(
            name='biodata',
        ),
        migrations.DeleteModel(
            name='room',
        ),
    ]
