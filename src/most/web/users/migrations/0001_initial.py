# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import most.web.utils
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MostUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(unique=True, max_length=30, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, verbose_name='User email address')),
                ('first_name', models.CharField(max_length=50, verbose_name='User first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='User last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is the user active?')),
                ('is_staff', models.BooleanField(default=True, verbose_name='Is the user staff?')),
                ('birth_date', models.DateField(null=True, verbose_name='User birth date', blank=True)),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is the user superuser?')),
                ('uuid', models.CharField(default=most.web.utils.pkgen, unique=True, max_length=40)),
                ('numeric_password', models.CharField(help_text='5 numbers code', max_length=5, null=True, verbose_name='Numeric password', blank=True)),
                ('user_type', models.CharField(default=b'ST', max_length=2, verbose_name='User type', choices=[(b'AD', 'Administrative'), (b'TE', 'Technician'), (b'CL', 'Clinician'), (b'ST', 'Student')])),
                ('gender', models.CharField(default=b'U', max_length=1, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female'), (b'U', 'Unknown')])),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Phone', blank=True)),
                ('mobile', models.CharField(max_length=20, null=True, verbose_name='Mobile phone', blank=True)),
                ('certified_email', models.EmailField(max_length=75, null=True, verbose_name='Certified email', blank=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_modified_timestamp', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ClinicianUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clinician_type', models.CharField(max_length=2, verbose_name='Clinician type', choices=[(b'DR', 'Doctor'), (b'OP', 'Operator')])),
                ('specialization', models.CharField(max_length=50, null=True, verbose_name='Clinical specialization', blank=True)),
                ('is_health_care_provider', models.BooleanField(default=True, verbose_name='Is health care provider?')),
                ('user', models.ForeignKey(related_name='clinician_related', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
            options={
                'db_table': 'most_clinician_user',
                'verbose_name': 'Clinician User',
                'verbose_name_plural': 'Clinician Users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TaskGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('description', models.CharField(help_text='e.g. "Pediatric Cardiology"', max_length=100, verbose_name='Description')),
                ('task_group_type', models.CharField(max_length=2, verbose_name='Task group type', choices=[(b'SP', b'Service Provider'), (b'HF', b'Health Care Facility')])),
                ('hospital', models.CharField(default=None, max_length=100, null=True, verbose_name='Hospital', blank=True)),
                ('is_health_care_provider', models.BooleanField(default=True, verbose_name='Is health care provider?')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active?')),
                ('uuid', models.CharField(default=most.web.utils.pkgen, unique=True, max_length=40)),
                ('related_task_groups', models.ManyToManyField(related_name='specialist_task_group', null=True, to='users.TaskGroup', blank=True)),
                ('users', models.ManyToManyField(related_name='task_group_related', null=True, verbose_name='MOST Users', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'db_table': 'most_task_group',
                'verbose_name': 'Task Group',
                'verbose_name_plural': 'Task Groups',
            },
            bases=(models.Model,),
        ),
    ]
