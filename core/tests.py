import shutil
import tempfile
from io import BytesIO

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from PIL import Image

from core.models import Photo


class PhotoThumbnailTests(TestCase):
    def setUp(self):
        self.media_root = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.media_root)

    def test_photo_save_generates_thumbnail(self):
        image_buffer = BytesIO()
        Image.new("RGB", (1200, 800), "#ffb900").save(image_buffer, format="JPEG")
        image = SimpleUploadedFile(
            "photo.jpg",
            image_buffer.getvalue(),
            content_type="image/jpeg",
        )

        with override_settings(MEDIA_ROOT=self.media_root):
            photo = Photo.objects.create(title="Test photo", image=image, order=1)

            self.assertTrue(photo.thumbnail)
            self.assertEqual(
                photo.thumbnail.name,
                f"photos/thumbnails/{photo.pk}.jpg",
            )
            self.assertEqual(photo.thumbnail_url, photo.thumbnail.url)

            photo.thumbnail.open("rb")
            try:
                with Image.open(photo.thumbnail) as thumbnail:
                    self.assertLessEqual(thumbnail.width, 360)
                    self.assertLessEqual(thumbnail.height, 360)
            finally:
                photo.thumbnail.close()
