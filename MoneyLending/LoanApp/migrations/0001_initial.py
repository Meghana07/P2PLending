# Generated by Django 2.2.6 on 2020-05-24 18:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserApp', '0003_borrower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('loanID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('Amount', models.IntegerField()),
                ('InterestR', models.IntegerField()),
                ('time', models.IntegerField()),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UserApp.Borrower')),
            ],
        ),
    ]
