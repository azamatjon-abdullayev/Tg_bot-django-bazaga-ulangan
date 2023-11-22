# Generated by Django 4.2.4 on 2023-11-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('fam', models.CharField(blank=True, max_length=100, null=True)),
                ('usern', models.CharField(blank=True, max_length=100, null=True)),
                ('tg_id', models.IntegerField(unique=True)),
            ],
        ),
    ]