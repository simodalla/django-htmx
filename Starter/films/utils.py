from django.db.models import Max

from .models import UserFilms


def get_max_order(user) -> int:
    existing_films = UserFilms.objects.filter(user=user)
    if not existing_films.exists():
        return 1
    current_max = existing_films.aggregate(max_order=Max("order"))["max_order"]
    return current_max + 1
