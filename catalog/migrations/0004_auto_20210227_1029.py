# Generated by Django 3.1.6 on 2021-02-27 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='preview',
            field=models.ImageField(blank=True, upload_to='item_preview/', verbose_name='Preview'),
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Is active')),
                ('priority', models.PositiveIntegerField(verbose_name='Priority')),
                ('alt', models.CharField(max_length=150, verbose_name='Alt')),
                ('image', models.ImageField(blank=True, upload_to='item_image/', verbose_name='Image')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.item', verbose_name='Item')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'ordering': ('priority',),
            },
        ),
    ]
