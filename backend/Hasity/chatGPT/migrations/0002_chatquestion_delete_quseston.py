# Generated by Django 4.0.6 on 2022-12-08 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatGPT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatQuestion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quseston', models.TextField()),
                ('answer', models.TextField()),
                ('create_time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Quseston',
        ),
    ]