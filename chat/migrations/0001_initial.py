# Generated by Django 2.1.4 on 2018-12-18 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isInstructor', models.BooleanField()),
                ('userName', models.CharField(max_length=16)),
            ],
        ),
    ]
