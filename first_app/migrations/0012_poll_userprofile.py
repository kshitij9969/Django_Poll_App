# Generated by Django 3.0.3 on 2020-02-22 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0011_auto_20200222_1021'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'UserProfiles',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=100)),
                ('poll_count_yes', models.IntegerField()),
                ('poll_count_no', models.IntegerField()),
                ('Users', models.ManyToManyField(to='first_app.UserProfile')),
            ],
            options={
                'db_table': 'Polls',
            },
        ),
    ]
