# Generated by Django 3.2.7 on 2021-09-09 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('thumbnail', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('nameKor', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('yearPublished', models.IntegerField()),
                ('minPlayers', models.IntegerField()),
                ('maxPlayers', models.IntegerField()),
                ('minPlayTime', models.IntegerField()),
                ('maxPlayTime', models.IntegerField()),
                ('minAge', models.IntegerField()),
                ('category', models.TextField()),
                ('playType', models.TextField()),
                ('series', models.TextField()),
                ('designer', models.TextField()),
                ('artist', models.TextField()),
                ('publisher', models.TextField()),
                ('usersRated', models.IntegerField()),
                ('averageRate', models.FloatField()),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('comment', models.TextField()),
                ('gameName', models.CharField(max_length=100)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('gameId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boardGameRec.game')),
            ],
        ),
    ]
