# Generated by Django 4.2.3 on 2023-08-08 05:40

from django.db import migrations, models
import users.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/users')),
                ('first_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=250, null=True, unique=True)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', users.models.user.CustomUserManager()),
            ],
        ),
    ]
