# Generated by Django 3.1.3 on 2020-12-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('response_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModelAllTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_binary', models.BinaryField()),
                ('field_boolean', models.BooleanField()),
                ('field_null_boolean', models.NullBooleanField()),
                ('field_date', models.DateField()),
                ('field_time', models.TimeField()),
                ('field_datetime', models.DateTimeField()),
                ('field_duration', models.DurationField()),
                ('field_big_integer', models.BigIntegerField()),
                ('field_decimal', models.DecimalField(decimal_places=10, max_digits=12)),
                ('field_float', models.FloatField()),
                ('field_integer', models.IntegerField()),
                ('field_positive_integer', models.PositiveIntegerField()),
                ('field_positive_small_integer', models.PositiveSmallIntegerField()),
                ('field_small_integer', models.SmallIntegerField()),
                ('field_char', models.CharField(max_length=10)),
                ('field_text', models.TextField()),
                ('field_email', models.EmailField(max_length=254)),
                ('field_file', models.FileField(upload_to='')),
                ('field_file_path', models.FilePathField()),
                ('field_image', models.ImageField(upload_to='')),
                ('field_generic_ip_address', models.GenericIPAddressField()),
                ('field_slug', models.SlugField()),
                ('field_url', models.URLField()),
                ('field_uuid', models.UUIDField()),
            ],
        ),
    ]
