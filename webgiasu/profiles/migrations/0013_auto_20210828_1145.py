# Generated by Django 3.2.5 on 2021-08-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default95486216548123654894126.png', upload_to='avatar', verbose_name='Avatar:'),
        ),
        migrations.AlterField(
            model_name='user',
            name='more',
            field=models.TextField(blank=True, verbose_name='Mô tả:'),
        ),
    ]