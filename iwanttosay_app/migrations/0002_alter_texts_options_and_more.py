# Generated by Django 5.0.6 on 2024-06-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iwanttosay_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='texts',
            options={'verbose_name_plural': 'Texts'},
        ),
        migrations.RenameField(
            model_name='texts',
            old_name='data_added',
            new_name='date_added',
        ),
        migrations.AlterField(
            model_name='texts',
            name='password',
            field=models.IntegerField(),
        ),
    ]
