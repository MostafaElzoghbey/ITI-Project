# Generated by Django 4.2.5 on 2023-09-18 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authmansoura', '0001_initial'),
        ('students', '0004_alter_books_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrowbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authmansoura.myaccount')),
                ('borrbook', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.books')),
            ],
        ),
    ]
