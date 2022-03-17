# Generated by Django 2.2.16 on 2022-03-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220315_1824'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique follow',
        ),
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('following', 'user'), name='unique follow'),
        ),
    ]
