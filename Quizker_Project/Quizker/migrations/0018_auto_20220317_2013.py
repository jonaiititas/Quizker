# Generated by Django 2.1.5 on 2022-03-17 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizker', '0017_auto_20220317_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizattempt',
            name='completed',
        ),
        migrations.AddField(
            model_name='quizattempt',
            name='quesitonsCompleted',
            field=models.IntegerField(default=0),
        ),
    ]