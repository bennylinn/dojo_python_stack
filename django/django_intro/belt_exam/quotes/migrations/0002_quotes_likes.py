# Generated by Django 3.0.8 on 2020-07-29 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotes',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='quotes.User'),
        ),
    ]
