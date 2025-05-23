# Generated by Django 5.1.3 on 2024-12-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Ator',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('nome', models.CharField(max_length=200)),
                ('nascimento', models.DateField(blank=True, null=True)),
                (
                    'nacionalidade',
                    models.CharField(
                        blank=True,
                        choices=[('USA', 'Estados Unidos'), ('BRA', 'Brasil')],
                        max_length=100,
                        null=True,
                    ),
                ),
            ],
        ),
    ]
