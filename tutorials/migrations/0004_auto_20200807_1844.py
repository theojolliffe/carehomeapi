# Generated by Django 3.1 on 2020-08-07 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0003_auto_20200805_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carehome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Deaths', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Purchases',
        ),
    ]
