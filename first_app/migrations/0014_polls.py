# Generated by Django 3.0.3 on 2020-02-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('first_app', '0013_auto_20200222_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=50)),
                ('poll_description', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Polls',
            },
        ),
    ]
