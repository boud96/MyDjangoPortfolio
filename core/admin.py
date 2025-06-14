from django.contrib import admin

from core.models import (
    PersonalInfo,
    Job,
    Education,
    TypeSkill,
    Skill,
    Project,
    Photo,
    SocialMediaAccount,
    CVFile,
)


@admin.register(PersonalInfo)
class PersonalInfo(admin.ModelAdmin):
    list_display = (
        "identifier",
        "active",
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
        "company",
        "position",
        "description",
        "start_date",
        "end_date",
        "note",
    )


@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = (
        "position",
        "title",
        "description",
        "start_date",
        "end_date",
        "note",
    )


@admin.register(TypeSkill)
class TypeSkillAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "order",
        "color",
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


@admin.register(SocialMediaAccount)
class SocialMediaAccountAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "type",
        "url",
    )


@admin.register(CVFile)
class CVFileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "file",
        "active"
    )
