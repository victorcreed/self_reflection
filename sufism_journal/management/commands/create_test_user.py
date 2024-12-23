from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates a test user'

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(username='testuser', email='test@example.com', password='password')
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating user: {e}'))
