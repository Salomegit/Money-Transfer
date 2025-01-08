# Generated by Django 5.1.4 on 2025-01-08 11:00

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=20, unique=True)),
                ('balance', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_transactions', to='myapp.account')),
                ('source_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outgoing_transactions', to='myapp.account')),
            ],
        ),
    ]
