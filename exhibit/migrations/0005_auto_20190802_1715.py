# Generated by Django 2.2.1 on 2019-08-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0004_auto_20190528_1755'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='project',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='competition',
            name='title',
            field=models.CharField(default='No title', max_length=200),
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
