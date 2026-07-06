import uuid
from io import BytesIO

from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from markdownfield.models import MarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from PIL import Image, ImageOps


class PersonalInfo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    short_description = models.CharField(max_length=100, blank=True, null=True)
    about_me = MarkdownField(validator=VALIDATOR_STANDARD)
    driver_license = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    headshot = models.ImageField(upload_to='headshots/', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier

    @property
    def age(self):
        today = timezone.localdate()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day)
            < (self.date_of_birth.month, self.date_of_birth.day)
        )

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if self.active:
            PersonalInfo.objects.update(active=False)
        super().save(*args, **kwargs)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = MarkdownField(validator=VALIDATOR_STANDARD)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company

    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100)
    description = MarkdownField(validator=VALIDATOR_STANDARD)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']


class TypeSkill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    order = models.IntegerField(unique=True, default=1, validators=[MinValueValidator(1)])
    color = models.CharField(max_length=7, default="#000000")  # TODO: Add color picker - django-colorfield

    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = MarkdownField(validator=VALIDATOR_STANDARD, blank=True, null=True)
    percent = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    type_skill = models.ForeignKey(TypeSkill, on_delete=models.CASCADE)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']

    def clean(self, *args, **kwargs):
        obj = Skill.objects.filter(type_skill=self.type_skill).filter(order=self.order).exclude(id=self.id)
        if obj.exists():
            raise ValueError("Skill with this order already exists")


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)], unique=True)
    note = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-order']


class Photo(models.Model):
    THUMBNAIL_SIZE = (360, 360)

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    thumbnail = models.ImageField(
        upload_to='photos/thumbnails/',
        blank=True,
        null=True,
        editable=False,
    )
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)], unique=True)

    def __str__(self):
        return self.title

    @property
    def thumbnail_url(self):
        if self.thumbnail:
            return self.thumbnail.url
        return self.image.url

    def save(self, *args, **kwargs):
        old_image_name = None
        if self.pk:
            old_photo = Photo.objects.filter(pk=self.pk).only("image").first()
            if old_photo:
                old_image_name = old_photo.image.name

        super().save(*args, **kwargs)

        image_changed = old_image_name != self.image.name
        if self.image and (image_changed or not self.thumbnail):
            self.generate_thumbnail()

    def generate_thumbnail(self):
        self.image.open("rb")
        try:
            with Image.open(self.image) as image:
                image = ImageOps.exif_transpose(image)
                image.thumbnail(self.THUMBNAIL_SIZE, Image.Resampling.LANCZOS)

                if image.mode not in ("RGB", "L"):
                    image = image.convert("RGB")

                thumbnail_buffer = BytesIO()
                image.save(
                    thumbnail_buffer,
                    format="JPEG",
                    quality=82,
                    optimize=True,
                )
        finally:
            self.image.close()

        if self.thumbnail:
            self.thumbnail.storage.delete(self.thumbnail.name)

        thumbnail_name = f"{self.pk}.jpg"
        self.thumbnail.save(
            thumbnail_name,
            ContentFile(thumbnail_buffer.getvalue()),
            save=False,
        )
        Photo.objects.filter(pk=self.pk).update(thumbnail=self.thumbnail.name)

    class Meta:
        ordering = ['-order']


class SocialMediaAccount(models.Model):
    SOCIAL_MEDIA_ACCOUNT_TYPE = (
        (0, "LinkedIn"),
        (1, "Facebook"),
        (2, "Instagram"),
        (3, "GitHub"),
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    type = models.IntegerField(choices=SOCIAL_MEDIA_ACCOUNT_TYPE)
    owner = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.get_type_display()

    def clean(self, *args, **kwargs):
        obj = SocialMediaAccount.objects.filter(type=self.type).filter(owner=self.owner).exclude(id=self.id)
        if obj.exists():
            raise ValidationError("Social media account with this type already exists for this owner")


class CVFile(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='cv_files/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.active:
            CVFile.objects.update(active=False)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['name']
