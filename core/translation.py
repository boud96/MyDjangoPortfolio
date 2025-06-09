from modeltranslation.translator import register, TranslationOptions
from .models import Skill, PersonalInfo, Job, Education, TypeSkill, Project, Photo


@register(PersonalInfo)
class PersonalInfoTranslationOptions(TranslationOptions):
    fields = ('about_me',)


@register(Job)
class JobTranslationOptions(TranslationOptions):
    fields = ('position', 'description',)


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('position', 'description',)


@register(TypeSkill)
class TypeSkillTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description',)


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)
