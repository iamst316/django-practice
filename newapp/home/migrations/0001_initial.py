# Generated by Django 4.0.6 on 2022-07-28 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('details', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='pics')),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
