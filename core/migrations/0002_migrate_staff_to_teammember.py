from django.db import migrations

def copy_staff_to_teammembers(apps, schema_editor):
    BarberMembers = apps.get_model('core', 'BarberMembers')
    TattooMembers = apps.get_model('core', 'TattooMembers')
    TeamMembers = apps.get_model('core', 'TeamMembers')

    # Copy Barbers
    for barber in BarberMembers.objects.all():
        TeamMembers.objects.create(
            name=barber.name,
            role='barber',
            bio=barber.bio  # Include the bio field
        )

    # Copy Tattoo Artists and Piercers
    for tattooer in TattooMembers.objects.all():
        TeamMembers.objects.create(
            name=tattooer.name,
            role=tattooer.role,
            bio=tattooer.bio  # Include the bio field
        )

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(copy_staff_to_teammembers),
    ]
