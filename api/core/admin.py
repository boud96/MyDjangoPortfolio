from django.contrib import admin

from core.models import PersonalInfo, Job, Education, TypeSkill, Skill


@admin.register(PersonalInfo)
class PersonalInfo(admin.ModelAdmin):
    list_display = (
        "identifier",
        "created_on",
        "headshot",
        "title",
        "first_name",
        "last_name",
        "email",
        "address",
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
    )
