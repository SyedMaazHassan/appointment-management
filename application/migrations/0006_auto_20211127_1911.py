# Generated by Django 3.2.8 on 2021-11-27 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20211127_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='twitter_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='social_links',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.social'),
        ),
        migrations.AlterField(
            model_name='social',
            name='facebook_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='instagram_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='linkedin_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]