# Generated by Django 4.1 on 2022-09-13 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('ageGroup', models.CharField(max_length=50)),
                ('fees', models.DecimalField(decimal_places=2, max_digits=6)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('paymentMethod', models.CharField(max_length=200)),
                ('totalFees', models.DecimalField(decimal_places=2, max_digits=6)),
                ('isPaid', models.BooleanField(default=False)),
                ('paidAt', models.DateTimeField(null=True)),
                ('isAccepted', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
