# Generated by Django 3.1 on 2020-08-15 11:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('article_wiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
