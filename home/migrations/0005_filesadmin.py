# Generated by Django 3.1.5 on 2021-02-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_contact_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminupload', models.FileField(upload_to='media')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
