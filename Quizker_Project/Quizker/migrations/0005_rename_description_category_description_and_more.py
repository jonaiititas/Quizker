# Generated by Django 4.0.3 on 2022-03-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizker', '0004_alter_multiplechoice_options_alter_openended_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Correct',
            new_name='correct',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='openended',
            old_name='Answer',
            new_name='answer',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='Quiz',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='quiz',
            old_name='Title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='trueorfalse',
            old_name='Answer',
            new_name='answer',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='ChoiceID',
        ),
        migrations.RemoveField(
            model_name='question',
            name='QuestionID',
        ),
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]