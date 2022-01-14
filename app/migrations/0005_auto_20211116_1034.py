# Generated by Django 3.2.7 on 2021-11-16 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_subcategory_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcelFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='excel')),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]