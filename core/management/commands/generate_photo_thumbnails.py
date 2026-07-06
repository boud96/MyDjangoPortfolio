from django.core.management.base import BaseCommand

from core.models import Photo


class Command(BaseCommand):
    help = "Generate thumbnails for existing photo records."

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Regenerate thumbnails even when a thumbnail already exists.",
        )

    def handle(self, *args, **options):
        force = options["force"]
        created = 0
        skipped = 0
        failed = 0

        for photo in Photo.objects.exclude(image=""):
            if photo.thumbnail and not force:
                skipped += 1
                continue

            try:
                photo.generate_thumbnail()
            except Exception as exc:
                failed += 1
                self.stderr.write(
                    self.style.ERROR(
                        f"Failed to generate thumbnail for {photo.pk}: {exc}"
                    )
                )
                continue

            created += 1
            self.stdout.write(
                self.style.SUCCESS(f"Generated thumbnail for {photo.pk}")
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Done. Generated: {created}. Skipped: {skipped}. Failed: {failed}."
            )
        )
