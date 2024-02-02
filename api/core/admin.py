from django.contrib import admin

from core.models import (
    PersonalInfo,
    Job,
    Education,
    TypeSkill,
    Skill,
    Project,
    Photo,
)


@admin.register(PersonalInfo)
class PersonalInfo(admin.ModelAdmin):
    list_display = (
        "active",
        "identifier",
        "created_on",
        "first_name",
        "last_name",
        "title",
        "email",
        "address",
        "headshot",
    )


@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = (
        "title",
        "position",
        "description",
        "start_date",
        "end_date",
        "note",
    )


@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = (
        "title",
        "position",
        "description",
        "start_date",
        "end_date",
        "note",
    )


@admin.register(TypeSkill)
class TypeSkillAdmin(admin.ModelAdmin):
    list_display = (
        "title",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "type_skill",
        "order",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "short_description",
        "description",
        "image",
        "order",
    )


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "image",
        "order",
    )
