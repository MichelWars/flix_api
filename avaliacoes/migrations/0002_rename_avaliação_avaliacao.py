# Generated by Django 5.1.3 on 2024-12-06 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0001_initial'),
        ('filmes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Avaliação',
            new_name='Avaliacao',
        ),
    ]
