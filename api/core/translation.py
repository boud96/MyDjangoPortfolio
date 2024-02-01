from modeltranslation.translator import register, TranslationOptions
from .models import Skill


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('description',)
