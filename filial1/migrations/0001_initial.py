# Generated by Django 4.1.4 on 2022-12-08 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('card_number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('start_price', models.IntegerField()),
                ('type_of_cuisine', models.CharField(max_length=20)),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('extra_price', models.IntegerField()),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('position', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegetarian', models.BooleanField(default=True, null=True)),
                ('food_status', models.CharField(max_length=20, null=True)),
                ('final_price', models.IntegerField(null=True)),
                ('order_date_time', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filial1.client')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filial1.food')),
                ('ingridient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filial1.ingridient')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filial1.worker')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='orders',
            field=models.ManyToManyField(related_name='food', through='filial1.Order', to='filial1.ingridient'),
        ),
        migrations.CreateModel(
            name='Resultat',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('filial1.order',),
        ),
    ]
