# Generated by Django 4.1.7 on 2023-03-14 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('filling_status', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TaxCalculation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_income', models.FloatField()),
                ('federal_tax', models.FloatField()),
                ('filling_status', models.SmallIntegerField()),
                ('tax_bracket', models.DecimalField(decimal_places=2, max_digits=4)),
                ('single_start', models.DecimalField(decimal_places=2, max_digits=10)),
                ('single_end', models.DecimalField(decimal_places=2, max_digits=10)),
                ('married_start', models.DecimalField(decimal_places=2, max_digits=10)),
                ('married_end', models.DecimalField(decimal_places=2, max_digits=10)),
                ('charitable_contributions', models.FloatField()),
                ('college_expenses', models.FloatField()),
                ('student_loan_interest', models.FloatField()),
                ('taxes_registration', models.FloatField()),
                ('interest_taxes', models.FloatField()),
                ('medical_expenses', models.FloatField()),
                ('retirement_contributions', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taxes_registration', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('federal_tax', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Retirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retirement_contributions', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_expenses', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gross_income', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('own', models.BooleanField()),
                ('interest_taxes', models.FloatField(blank=True, null=True)),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrolled', models.BooleanField()),
                ('college_expenses', models.FloatField(blank=True, null=True)),
                ('scholarships_received', models.FloatField(blank=True, null=True)),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
        migrations.CreateModel(
            name='Charitable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charitable_contributions', models.FloatField()),
                ('demographics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CalApp.demographics')),
            ],
        ),
    ]
