# Generated by Django 5.0.7 on 2024-07-18 10:11

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_posts_author_posts_created_at_posts_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-publish']},
        ),
        migrations.AddField(
            model_name='posts',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default='DF', max_length=2),
        ),
        migrations.AddField(
            model_name='posts',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddIndex(
            model_name='posts',
            index=models.Index(fields=['-publish'], name='blogapp_pos_publish_7f82f8_idx'),
        ),
    ]
