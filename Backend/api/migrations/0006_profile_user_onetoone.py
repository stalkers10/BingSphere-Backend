import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def dedupe_profiles(apps, schema_editor):
    Profile = apps.get_model('api', 'Profile')
    seen_user_ids = set()

    for profile in Profile.objects.order_by('id'):
        if profile.user_id in seen_user_ids:
            profile.delete()
        else:
            seen_user_ids.add(profile.user_id)


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_force_watchlist_sqlite_repair'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(dedupe_profiles, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='profile',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
