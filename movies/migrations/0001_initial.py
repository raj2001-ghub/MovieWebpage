# Generated by Django 3.2.6 on 2021-10-26 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=200)),
                ('movie_genre', models.CharField(max_length=75)),
                ('movie_rating', models.IntegerField()),
                ('movie_yor', models.IntegerField()),
                ('movie_summary', models.CharField(max_length=500)),
            ],
        ),
    ]
