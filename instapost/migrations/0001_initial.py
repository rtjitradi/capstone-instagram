<<<<<<< HEAD
# Generated by Django 3.1.2 on 2020-10-18 02:09
=======
# Generated by Django 3.1.2 on 2020-10-18 01:46
>>>>>>> 2bcdf608b15eb876c10bc29b484c17e187dad0fc

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('caption', models.TextField(blank=True, max_length=70, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='static/post_upload/', verbose_name='picture')),
                ('liked', models.BooleanField(default=False)),
            ],
        ),
    ]
