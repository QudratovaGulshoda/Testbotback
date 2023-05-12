# Generated by Django 4.1.7 on 2023-04-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_testdone_false_answers_testdone_true_answers'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=150, verbose_name='Telegram ID')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Daily Test ',
                'verbose_name_plural': 'Daily Tests ',
            },
        ),
    ]
