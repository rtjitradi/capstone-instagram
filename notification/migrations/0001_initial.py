<<<<<<< HEAD
# Generated by Django 3.1.2 on 2020-10-18 02:09
=======
# Generated by Django 3.1.2 on 2020-10-18 01:46
>>>>>>> 2bcdf608b15eb876c10bc29b484c17e187dad0fc

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_flag', models.BooleanField(default=False)),
                ('post_receive', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.commentmodel')),
            ],
        ),
    ]
