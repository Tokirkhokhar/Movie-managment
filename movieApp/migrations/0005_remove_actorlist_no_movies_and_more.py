# Generated by Django 4.0.4 on 2022-04-22 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0004_alter_actorlist_id_alter_movielist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actorlist',
            name='no_movies',
        ),
        migrations.RemoveField(
            model_name='movielist',
            name='total_actors',
        ),
    ]
