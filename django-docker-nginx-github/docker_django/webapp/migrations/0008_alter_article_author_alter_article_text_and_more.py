# Generated by Django 4.1.5 on 2023-01-26 20:35

from django.db import migrations, models
import webapp.validate.validate_fields


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_remove_article_tags_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default='Unknown', max_length=40, validators=[webapp.validate.validate_fields.MinLengthValidator(5)], verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=3000, validators=[webapp.validate.validate_fields.MinLengthValidator(5)], verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, validators=[webapp.validate.validate_fields.MinLengthValidator(5)], verbose_name='Заголовок'),
        ),
    ]