# Generated by Django 3.1.5 on 2021-01-10 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210108_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='influencers', to='api.account'),
        ),
    ]
