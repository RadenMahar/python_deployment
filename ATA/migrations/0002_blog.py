# Generated by Django 2.2.3 on 2019-07-24 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('head', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]
