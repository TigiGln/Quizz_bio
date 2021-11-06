# Generated by Django 3.0.3 on 2021-10-31 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('image_name', models.IntegerField()),
                ('description', models.TextField()),
                ('microscopy', models.CharField(max_length=400)),
                ('cell_type', models.CharField(max_length=300)),
                ('component', models.CharField(max_length=150)),
                ('doi', models.CharField(max_length=450)),
                ('organism', models.CharField(max_length=500)),
            ],
        ),
    ]
