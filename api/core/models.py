import uuid

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

    def __str__(self):
        return self.identifier

    class Meta:
        ordering = ['-created_on']


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

    def __str__(self):
        return self.title


class Skill(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()  # TODO RichTextField to allow bold, italic, underline, etc.
    type_skill = models.ForeignKey(TypeSkill, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-title']
