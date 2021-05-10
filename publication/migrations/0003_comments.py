# Generated by Django 3.1.7 on 2021-03-13 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publication', '0002_auto_20210311_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
                ('publications', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='publication.publications')),
            ],
        ),
    ]
