# Generated by Django 4.1.7 on 2023-02-19 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_post_options_post_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='url_name',
            field=models.CharField(auto_created=True, default=models.CharField(max_length=200), max_length=200),
        ),
    ]
