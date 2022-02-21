# Generated by Django 4.0.2 on 2022-02-21 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='post',
            name='minutes_to_read',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Минут на прочтение'),
        ),
    ]
