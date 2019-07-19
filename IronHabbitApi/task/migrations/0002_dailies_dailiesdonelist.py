# Generated by Django 2.1.9 on 2019-07-19 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dailies',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='task.Task')),
            ],
            bases=('task.task',),
        ),
        migrations.CreateModel(
            name='DailiesDoneList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('state', models.BooleanField()),
                ('dailies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Dailies')),
            ],
        ),
    ]
