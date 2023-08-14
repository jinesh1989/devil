# Generated by Django 4.2.4 on 2023-08-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('note', models.TextField(max_length=1200)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]