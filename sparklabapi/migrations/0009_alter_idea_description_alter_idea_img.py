# Generated by Django 4.1.3 on 2024-09-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sparklabapi', '0008_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='idea',
            name='img',
            field=models.URLField(max_length=800),
        ),
    ]