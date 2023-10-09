# Generated by Django 4.2.3 on 2023-10-09 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letsbright', '0004_userprofile_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='audience_type',
            field=models.CharField(blank=True, choices=[('new_nihilist', 'The New Nihilists'), ('pioneer', 'The Pioneers'), ('time_keeper', 'The Time Keepers'), ('reductionist', 'The Reductionists'), ('dreamer', 'The Dreamers'), ('rebel', 'The Rebels'), ('Maestro', 'Design Maestros'), ('builder', 'The Builders')], max_length=50),
        ),
    ]
