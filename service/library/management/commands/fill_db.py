import json
import os

from django.conf import settings
from django.core.management import BaseCommand

from library.models import Author
from userapp.models import User

JSON_PATH = os.path.join(settings.BASE_DIR, 'library/json')


def load_json_data(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json')) as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = load_json_data('authors')
        Author.objects.all().delete()
        for author in authors:
            Author.objects.create(**author)

        users = load_json_data('users')
        User.objects.all().delete()
        for user in users:
            User.objects.create(**user)

        # User.objects.create_superuser('admin', 'django@geekbrains.local', 'geekbrains')
