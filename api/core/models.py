import uuid

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PersonalInfo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_on = models.DateTimeField(auto_now_add=True)
    identifier = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    about_me = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    driver_license = models.CharField(max_length=32)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    headshot = models.ImageField(upload_to='headshots/', blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        if self.active:
            PersonalInfo.objects.update(active=False)
        super().save(*args, **kwargs)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    start_date = models.DateField()
    end_date = models.DateField()
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']


class Education(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # TODO RichTextField to allow bold, italic, underline, etc.
    start_date = models.DateField()
    end_date = models.DateField()
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
    description = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    percent = models.IntegerField(default=100, validators=[MinValueValidator(1), MaxValueValidator(100)])
    type_skill = models.ForeignKey(TypeSkill, on_delete=models.CASCADE)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']

    def save(self, *args, **kwargs):
        obj = Skill.objects.filter(type_skill=self.type_skill).filter(order=self.order).exclude(id=self.id)
        if obj.exists():
            raise ValueError("Skill with this order already exists")
        super().save(*args, **kwargs)


class Project(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    description = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)], unique=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-order']


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/')
    order = models.IntegerField(default=1, validators=[MinValueValidator(1)], unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-order']
