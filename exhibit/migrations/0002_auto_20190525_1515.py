# Generated by Django 2.2.1 on 2019-05-25 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exhibit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='atelier',
            name='atelier_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='competition',
            name='competition_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='publication',
            name='publication_text',
            field=models.TextField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_title', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibit.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exhibit.Project')),
            ],
        ),
    ]
