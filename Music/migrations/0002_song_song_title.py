# Generated by Django 2.0.7 on 2018-07-24 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_title',
            field=models.CharField(default='annointing', max_length=430),
        ),
    ]
