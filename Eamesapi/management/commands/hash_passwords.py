from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class Command(BaseCommand):
    help = 'Updates user passwords with hashed versions'

    def handle(self, *args, **options):
        users = User.objects.all()
        updated_count = 0
        for user in users:
            user.password = make_password('password')  # Replace 'password' with the actual password if different
            user.save()
            updated_count += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully updated {updated_count} user passwords'))

        # Optionally, print out the first user's hashed password as a check
        if users.exists():
            first_user = users.first()
            self.stdout.write(f"First user ({first_user.username}) hashed password: {first_user.password}")