import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from shop.models import VideoCard


ITEMS = [
    ("NVIDIA GeForce RTX 5090", 230000.00, "Учебная позиция для демонстрации карточки товара."),
    ("NVIDIA GeForce RTX 4090", 165000.00, "Учебная позиция для демонстрации API."),
    ("NVIDIA GeForce RTX 5080", 130000.00, "Учебная позиция для демонстрации HTMX."),
    ("AMD Radeon RX 9070 XT", 95000.00, "Учебная позиция для проверки PostgreSQL."),
    ("NVIDIA GeForce RTX 4080 Super", 115000.00, "Учебная позиция без реальной продажи."),
]

for name, price, description in ITEMS:
    VideoCard.objects.update_or_create(
        name=name,
        defaults={"price": price, "description": description},
    )

print("Учебные данные загружены.")
