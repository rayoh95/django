# Generated by Django 3.0.8 on 2020-08-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boards', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='photo',
        ),
        migrations.AddField(
            model_name='board',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image'),
        ),
    ]
