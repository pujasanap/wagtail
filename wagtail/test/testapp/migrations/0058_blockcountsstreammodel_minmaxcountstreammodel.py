# Generated by Django 2.1.7 on 2019-03-28 02:30

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.contrib.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0057_customdocumentwithauthor'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockCountsStreamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.fields.StreamField([('text', wagtail.blocks.CharBlock()), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.contrib.images.blocks.ImageChooserBlock())])),
            ],
        ),
        migrations.CreateModel(
            name='MinMaxCountStreamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', wagtail.fields.StreamField([('text', wagtail.blocks.CharBlock()), ('rich_text', wagtail.blocks.RichTextBlock()), ('image', wagtail.contrib.images.blocks.ImageChooserBlock())])),
            ],
        ),
    ]
