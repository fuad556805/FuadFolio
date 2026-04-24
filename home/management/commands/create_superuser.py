from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='fuad').exists():
            User.objects.create_superuser('fuad', 'fuad@email.com', 'fuad1234')
            self.stdout.write('Superuser created!')
        else:
            self.stdout.write('Superuser already exists.')