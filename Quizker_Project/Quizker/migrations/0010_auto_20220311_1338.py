# Generated by Django 2.1.5 on 2022-03-11 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizker', '0009_auto_20220311_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, upload_to='Question_Images'),
        ),
    ]
