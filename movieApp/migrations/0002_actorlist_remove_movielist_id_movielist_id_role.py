# Generated by Django 4.0.4 on 2022-04-22 04:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actorlist',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('birthdate', models.DateField()),
                ('no_movies', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='id',
        ),
        migrations.AddField(
            model_name='movielist',
            name='Id',
            field=models.AutoField( primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.actorlist')),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieApp.movielist')),
            ],
        ),
    ]
