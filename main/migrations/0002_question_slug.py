# Generated by Django 3.1.1 on 2020-10-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='question'),
            preserve_default=False,
        ),
    ]
