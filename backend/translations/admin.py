from django.contrib import admin
from .models import Translation, FavoriteLang, User

# Rejestrujemy Twoje tabele, żeby były widoczne w panelu
admin.site.register(Translation)
admin.site.register(FavoriteLang)
admin.site.register(User)