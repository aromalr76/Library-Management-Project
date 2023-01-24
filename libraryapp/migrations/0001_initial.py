# Generated by Django 4.1.4 on 2023-01-19 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_phno', models.BigIntegerField()),
                ('student_sem', models.CharField(max_length=20)),
                ('student_password', models.CharField(max_length=20)),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='IssueBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('bk_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.books')),
                ('std_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.student')),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.course'),
        ),
    ]
