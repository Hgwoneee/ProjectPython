from ...utils import fetch_and_save_charging_stations
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetch charging stations data and save to database'

    def handle(self, *args, **kwargs):
        api_key = "EpUhD8WnDkKZKfH5rj1U7C9Y5hCObQbwGjbEU00ZYw0lWevnETv7%2BlHjECr%2F0%2BJaWN9K1SW10Fzj8IsBkaGOWQ%3D%3D"
        fetch_and_save_charging_stations(api_key)
