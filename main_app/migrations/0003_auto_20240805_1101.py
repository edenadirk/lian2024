# Generated by Django 5.0.4 on 2024-08-05 11:01

from django.db import migrations

def transfer_profile_to_temp(apps, schema_editor):
    Profile = apps.get_model('main_app', 'Profile')
    TempProfileData = apps.get_model('main_app', 'TempProfileData')
    
    for profile in Profile.objects.all():
        TempProfileData.objects.create(
            user_id=profile.user_id,
            date_of_birth=profile.date_of_birth,
            photo=profile.photo,
            location=profile.location,
            bio=profile.bio
        )

def reverse_transfer(apps, schema_editor):
    TempProfileData = apps.get_model('main_app', 'TempProfileData')
    TempProfileData.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_initial'),
    ]

    operations = [
        migrations.RunPython(transfer_profile_to_temp, reverse_transfer),
    ]
