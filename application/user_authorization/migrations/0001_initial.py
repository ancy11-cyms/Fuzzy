# Generated by Django 4.0.2 on 2022-03-03 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_Name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=10)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='resumedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, null=True)),
                ('Qualification', models.CharField(max_length=20)),
                ('Expireance', models.CharField(max_length=2)),
                ('Skills', models.CharField(max_length=50)),
                ('Picture', models.ImageField(upload_to='userpic/')),
                ('Marks', models.CharField(max_length=2)),
                ('Hobbies', models.CharField(max_length=30)),
                ('objj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_authorization.login')),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='loginobj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_authorization.registrations'),
        ),
    ]
