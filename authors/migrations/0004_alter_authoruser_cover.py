# Generated by Django 5.1.1 on 2024-10-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_alter_authoruser_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authoruser',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/user/%Y/%m/%d/'),
        ),
    ]