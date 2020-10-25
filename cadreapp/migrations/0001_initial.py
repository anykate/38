# Generated by Django 3.1.2 on 2020-10-24 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Upazila',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadreapp.district')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadreapp.division')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadreapp.division'),
        ),
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_Name_EN', models.CharField(max_length=100)),
                ('full_Name_BN', models.CharField(max_length=100)),
                ('nick_Name', models.CharField(max_length=60)),
                ('fathers_Name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('mobile_Number', models.CharField(max_length=11, unique=True)),
                ('post_Code', models.PositiveSmallIntegerField()),
                ('date_of_Birth', models.DateField()),
                ('national_ID', models.IntegerField(unique=True)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hinduism', 'Hinduism'), ('Christianity', 'Christianity'), ('Buddhism', 'Buddhism'), ('Other', 'Other')], max_length=45)),
                ('blood_Group', models.CharField(choices=[('A+', 'A+'), ('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('O-', 'O-'), ('B-', 'B-'), ('AB-', 'AB-')], max_length=5)),
                ('marital_Status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], max_length=10)),
                ('bCS_Registration_No', models.PositiveSmallIntegerField()),
                ('Merit_Position', models.PositiveSmallIntegerField(blank=True)),
                ('desire_Posting_Place', models.CharField(choices=[('DAE HQ', 'DAE HQ'), ('Agriculture Training Institute (ATI)', 'Agriculture Training Institute (ATI)'), ('Horticulture Centre', 'Horticulture Centre'), ('Plant Quarantine Station', 'Plant Quarantine Stations'), ('National Agriculture Training Academy (NATA)', 'National Agriculture Training Academy (NATA)'), ('Agriculture Information Service (AIS)', 'Agriculture Information Service (AIS)'), ('Seed Certification Agency (SCA)', 'Seed Certification Agency (SCA)'), ('Other', 'Other')], max_length=300)),
                ('hSC_Passing_Year', models.IntegerField(choices=[('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')])),
                ('college_Name', models.CharField(max_length=200)),
                ('graduation_Year', models.IntegerField(choices=[('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019')])),
                ('university_Name', models.CharField(choices=[('Bangladesh Agricultural University', 'Bangladesh Agricultural University'), ('Hajee Mohammad Danesh Science and Technology University', 'Hajee Mohammad Danesh Science and Technology University'), ('Khulna University', 'Khulna University'), ('Noakhali Science and Technology University', 'Noakhali Science and Technology University'), ('Patuakhali Science & Technology University', 'Patuakhali Science & Technology University'), ('University of Rajshahi', 'University of Rajshahi'), ('Sher-e-Bangla Agricultural University', 'Sher-e-Bangla Agricultural University'), ('Sylhet Agricultural University', 'Sylhet Agricultural University'), ('Others', 'Others')], max_length=100)),
                ('masters_Degree_if_any', models.CharField(blank=True, max_length=255)),
                ('university_or_Institute', models.CharField(blank=True, choices=[('Bangladesh Agricultural University', 'Bangladesh Agricultural University'), ('Hajee Mohammad Danesh Science and Technology University', 'Hajee Mohammad Danesh Science and Technology University'), ('Khulna University', 'Khulna University'), ('Noakhali Science and Technology University', 'Noakhali Science and Technology University'), ('Patuakhali Science & Technology University', 'Patuakhali Science & Technology University'), ('University of Rajshahi', 'University of Rajshahi'), ('Sher-e-Bangla Agricultural University', 'Sher-e-Bangla Agricultural University'), ('Sylhet Agricultural University', 'Sylhet Agricultural University'), ('Others', 'Others')], max_length=100)),
                ('previous_Job_if_any', models.CharField(blank=True, max_length=255)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadreapp.district')),
                ('division', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadreapp.division')),
                ('upazila', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadreapp.upazila')),
            ],
        ),
    ]
