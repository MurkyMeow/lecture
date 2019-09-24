# Generated by Django 2.2.1 on 2019-09-22 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0010_comment_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Course'),
        ),
        migrations.AddField(
            model_name='slide',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.Course'),
        ),
    ]