from django.core.management.base import BaseCommand
from hits.models import Artist, Hit
from typing import Any, TypeVar
from django.db.models.manager import BaseManager


class Command(BaseCommand):
    help = "Populate the database with initial data"

    TModel = TypeVar("TModel")

    def _get_or_create_bulk(
        self,
        model_manager: BaseManager[TModel],
        models_data: list[dict[str, Any]],
    ):
        for model_data in models_data:
            model, was_created = model_manager.get_or_create(**model_data)
            if was_created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"{str(model.__class__)} {model} created successfully"
                    )
                )

    def handle(self, *args, **kwargs):
        artists_data = [
            {"first_name": "Kaliber 44", "last_name": ""},
            {
                "first_name": "Adam 'Łona'",
                "last_name": "Zieliński",
            },
            {
                "first_name": "Paktofonika",
                "last_name": "",
            },
        ]
        self._get_or_create_bulk(Artist.objects, artists_data)

        # Get artist instances
        kaliber44 = Artist.objects.get(first_name="Kaliber 44")
        lona = Artist.objects.get(first_name="Adam 'Łona'")
        paktofonika = Artist.objects.get(first_name="Paktofonika")

        hits_data = [
            # Kaliber 44 hits
            {"title": "Plus i minus", "artist": kaliber44},
            {"title": "Konfrontacje", "artist": kaliber44},
            {"title": "Księga Tajemnicza. Prolog", "artist": kaliber44},
            {"title": "6 czerwca", "artist": kaliber44},
            {"title": "Ułamek tarcia", "artist": kaliber44},
            {"title": "44", "artist": kaliber44},
            {"title": "W imię zasad", "artist": kaliber44},
            # Łona hits
            {"title": "Nic dziwnego", "artist": lona},
            {"title": "To nic nie znaczy", "artist": lona},
            {"title": "PAN DAREK", "artist": lona},
            {"title": "Błąd", "artist": lona},
            {"title": "KOCYK", "artist": lona},
            {"title": "Rozmowa", "artist": lona},
            # Paktofonika hits
            {"title": "Jestem Bogiem", "artist": paktofonika},
            {"title": "Ja to ja", "artist": paktofonika},
            {"title": "Chwile ulotne", "artist": paktofonika},
            {"title": "Kim jestem?", "artist": paktofonika},
            {"title": "2 Kilo", "artist": paktofonika},
            {"title": "Gdy nie ma dzieci", "artist": paktofonika},
            {"title": "Przebudzenie", "artist": paktofonika},
        ]
        self._get_or_create_bulk(Hit.objects, hits_data)
