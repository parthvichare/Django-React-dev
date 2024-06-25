# Generated by Django 5.0.6 on 2024-06-17 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_perfect_alter_post_comment_line'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment_line',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='perfect',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='area_sqft',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='post',
            name='beds',
            field=models.IntegerField(default=2, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='floor',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='post',
            name='furnishing',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='super_areas',
            field=models.CharField(default='', max_length=100),
        ),
    ]