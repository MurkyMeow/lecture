# Generated by Django 2.2.1 on 2019-08-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_comment_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='for_article',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]