# Generated by Django 3.2 on 2021-05-13 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('item_pic', models.ImageField(upload_to='item_pic')),
                ('price', models.IntegerField()),
                ('digital', models.BooleanField()),
                ('status', models.BooleanField(default=False)),
                ('days', models.IntegerField()),
                ('category', models.CharField(choices=[('General', 'General'), ('Electronic', 'Electronic'), ('Books', 'Books')], max_length=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='getter', to=settings.AUTH_USER_MODEL)),
                ('item', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.item')),
            ],
        ),
        migrations.CreateModel(
            name='Todoitem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
