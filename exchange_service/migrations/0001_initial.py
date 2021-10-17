# Generated by Django 3.1.7 on 2021-04-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]