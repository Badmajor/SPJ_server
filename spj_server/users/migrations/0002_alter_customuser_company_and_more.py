# Generated by Django 4.2.8 on 2023-12-28 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_rename_responsible_customer_manager'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pr_language',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.programminglanguage'),
        ),
    ]
