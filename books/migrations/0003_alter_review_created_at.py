# Generated by Django 4.1.3 on 2022-12-26 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
