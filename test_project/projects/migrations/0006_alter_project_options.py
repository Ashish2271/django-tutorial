# Generated by Django 4.1.7 on 2023-09-16 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_alter_project_options_alter_review_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_total', '-vote_ratio', 'title']},
        ),
    ]
