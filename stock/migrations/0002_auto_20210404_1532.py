# Generated by Django 3.1.7 on 2021-04-04 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('member_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='MemberType',
            fields=[
                ('member_type_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('member_type_description', models.CharField(max_length=50)),
                ('member_type_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
        migrations.AddField(
            model_name='members',
            name='member_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.membertype'),
        ),
    ]