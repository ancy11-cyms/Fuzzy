# Generated by Django 4.0.2 on 2022-02-24 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
            ],
        ),
    ]
