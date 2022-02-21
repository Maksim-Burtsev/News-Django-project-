# Generated by Django 4.0.2 on 2022-02-21 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'публикация', 'verbose_name_plural': 'публикации'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'публикация', 'verbose_name_plural': 'публикации'},
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='quantity_words',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество слов'),
        ),
    ]
