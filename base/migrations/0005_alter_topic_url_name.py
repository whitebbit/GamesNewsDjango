# Generated by Django 4.1.7 on 2023-02-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_topic_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='url_name',
            field=models.CharField(auto_created=True, default='<django.db.models.fields.charfield>', max_length=200),
        ),
    ]
