# Generated by Django 2.1.2 on 2018-10-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trabajos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('autor', models.CharField(max_length=40)),
                ('categoria', models.CharField(choices=[('CC', 'Ciencias Computacionales'), ('CT', 'Ciencias de la Tierra'), ('CN', 'Ciencias Naturales'), ('CS', 'Ciencias Sociales'), ('CM', 'Ciencias Medicas')], max_length=1)),
            ],
        ),
    ]