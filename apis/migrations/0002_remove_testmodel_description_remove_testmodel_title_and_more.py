# Generated by Django 4.0.5 on 2022-06-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='title',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='subcatgeory',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
